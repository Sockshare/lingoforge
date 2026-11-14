"""
LingoForge // Standalone Polyglot & Forge AI Studio Flask Server (Port 8103)
Provides REST APIs, SQLite state persistence, Forge AI Studio endpoints, and Neural Edge-TTS Audio.
"""

import asyncio
import hashlib
import os
from pathlib import Path
from flask import Flask, jsonify, render_template, request, send_file

from curriculum_data import LANGUAGES
from lingo_engine import LingoForgeEngine

BASE_DIR = Path(__file__).resolve().parent
TTS_CACHE_DIR = BASE_DIR / "data" / "tts"
TTS_CACHE_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
engine = LingoForgeEngine()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "app": "LingoForge // Polyglot & Forge AI Studio", "port": 8103})


@app.route("/api/state", methods=["GET"])
def get_state():
    return jsonify(engine.get_full_state())


@app.route("/api/dispatch", methods=["POST"])
def dispatch_action():
    body = request.get_json(silent=True) or {}
    action = body.get("action", "")
    payload = body.get("payload", body)
    res = engine.dispatch(action, payload)
    return jsonify(res)


@app.route("/api/explain_answer", methods=["POST"])
def explain_answer():
    body = request.get_json(silent=True) or {}
    res = engine.explain_my_answer(
        lang_code=body.get("lang_code", "es"),
        prompt=body.get("prompt", ""),
        user_answer=body.get("user_answer", ""),
        correct_answer=body.get("correct_answer", ""),
        base_explanation=body.get("explanation", ""),
    )
    return jsonify({"ok": True, "explanation": res})


@app.route("/api/roleplay", methods=["POST"])
def roleplay():
    body = request.get_json(silent=True) or {}
    res = engine.roleplay_turn(
        lang_code=body.get("lang_code", "es"),
        scenario_id=body.get("scenario_id", "es_rp_cafe"),
        user_message=body.get("message", ""),
        history=body.get("history", []),
    )
    return jsonify({"ok": True, **res})


@app.route("/api/generate_unit", methods=["POST"])
def generate_unit():
    body = request.get_json(silent=True) or {}
    res = engine.generate_custom_unit(
        lang_code=body.get("lang_code", "es"),
        topic=body.get("topic", "Night Market & Street Food"),
    )
    return jsonify(res)


async def _synthesize_edge_tts(text: str, voice: str, rate: str, out_path: Path) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(str(out_path))


def _synthesize_gtts_fallback(text: str, lang_code: str, slow: bool, out_path: Path) -> None:
    from gtts import gTTS

    gtts_lang_map = {"zh": "zh-CN"}
    g_lang = gtts_lang_map.get(lang_code, lang_code)
    tts = gTTS(text=text, lang=g_lang, slow=slow)
    tts.save(str(out_path))


@app.route("/api/tts", methods=["GET"])
def tts_endpoint():
    text = (request.args.get("text") or "").strip()
    lang_code = (request.args.get("lang") or "es").strip()
    gender = (request.args.get("gender") or "female").strip()
    slow = request.args.get("slow", "0") == "1"

    if not text:
        return jsonify({"ok": False, "error": "Missing text"}), 400

    # Strip parenthetical romanization so TTS reads only the native script
    clean_text = text.split("(")[0].strip() or text
    lang_cfg = LANGUAGES.get(lang_code, LANGUAGES["es"])
    voice = lang_cfg["voice_male"] if gender == "male" else lang_cfg["voice_female"]
    rate = "-35%" if slow else "+0%"

    digest = hashlib.sha256(f"{voice}|{rate}|{clean_text}".encode("utf-8")).hexdigest()[:24]
    cached_mp3 = TTS_CACHE_DIR / f"{lang_code}_{digest}.mp3"

    if not cached_mp3.exists() or cached_mp3.stat().st_size == 0:
        try:
            asyncio.run(_synthesize_edge_tts(clean_text, voice, rate, cached_mp3))
        except Exception:
            try:
                _synthesize_gtts_fallback(clean_text, lang_code, slow, cached_mp3)
            except Exception as exc2:
                return jsonify({"ok": False, "fallback_browser_tts": True, "reason": str(exc2)}), 200

    if cached_mp3.exists() and cached_mp3.stat().st_size > 0:
        return send_file(str(cached_mp3), mimetype="audio/mpeg")

    return jsonify({"ok": False, "fallback_browser_tts": True}), 200


@app.route("/api/speech_verify", methods=["POST"])
def speech_verify_endpoint():
    """Transcribes user microphone audio via ffmpeg + SpeechRecognition and verifies it against the target sentence."""
    import re
    import subprocess
    import tempfile

    lang_code = (request.form.get("lang_code") or "es").strip()
    target_sentence = (request.form.get("target_sentence") or "").strip()
    browser_transcript = (request.form.get("browser_transcript") or "").strip()
    audio_file = request.files.get("audio")

    lang_cfg = LANGUAGES.get(lang_code, LANGUAGES["es"])
    speech_lang = lang_cfg.get("speech_lang", "es-ES")

    transcribed_target = ""
    transcribed_en = ""
    max_volume_db = -91.0

    if audio_file:
        with tempfile.TemporaryDirectory() as tmpdir:
            in_path = Path(tmpdir) / "input_audio.webm"
            wav_path = Path(tmpdir) / "converted.wav"
            audio_file.save(str(in_path))

            # Measure peak volume (dB) of incoming audio stream
            v_proc = subprocess.run(
                ["ffmpeg", "-i", str(in_path), "-af", "volumedetect", "-f", "null", "/dev/null"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            m_vol = re.search(r"max_volume:\s*([-\d.]+)\s*dB", v_proc.stderr or "")
            if m_vol:
                try:
                    max_volume_db = float(m_vol.group(1))
                except ValueError:
                    max_volume_db = -91.0

            # Convert browser WebM/Opus/WAV to 16kHz mono PCM WAV with volume boost & silence trimming
            proc = subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    str(in_path),
                    "-af",
                    "highpass=f=80,lowpass=f=7500,volume=2.4",
                    "-ar",
                    "16000",
                    "-ac",
                    "1",
                    str(wav_path),
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if proc.returncode == 0 and wav_path.exists() and wav_path.stat().st_size > 200 and max_volume_db > -75.0:
                import speech_recognition as sr

                recognizer = sr.Recognizer()
                with sr.AudioFile(str(wav_path)) as src:
                    audio_data = recognizer.record(src)
                try:
                    transcribed_target = recognizer.recognize_google(audio_data, language=speech_lang)
                except Exception:
                    transcribed_target = ""
                try:
                    transcribed_en = recognizer.recognize_google(audio_data, language="en-US")
                except Exception:
                    transcribed_en = ""

    res = engine.verify_spoken_pronunciation(
        lang_code=lang_code,
        target_sentence=target_sentence,
        transcribed_target=transcribed_target or browser_transcript,
        transcribed_en=transcribed_en,
    )
    res["max_volume_db"] = max_volume_db
    res["crd_mic_muted"] = bool(max_volume_db <= -80.0 and not (transcribed_target or transcribed_en or browser_transcript))

    # If a remote PC browser (on https://julianmorrisette.c.googlers.com:8443) just verified speech, store it so the VM browser syncs automatically!
    if not res["crd_mic_muted"] and (transcribed_target or transcribed_en or browser_transcript):
        import time as _t

        app.config["LATEST_REMOTE_SPEECH"] = {
            "ts": _t.time(),
            "target_sentence": target_sentence,
            "result": res,
        }

    return jsonify({"ok": True, **res})


@app.route("/api/speech_latest", methods=["GET"])
def speech_latest_endpoint():
    """Allows the VM browser to automatically pick up voice verifications recorded from the user's PC browser."""
    latest = app.config.get("LATEST_REMOTE_SPEECH")
    return jsonify({"ok": True, "latest": latest})


if __name__ == "__main__":
    import threading
    from werkzeug.serving import make_server

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8103))
    https_port = int(os.environ.get("HTTPS_PORT", 8443))

    cert_file = BASE_DIR / "data" / "ssl" / "cert.pem"
    key_file = BASE_DIR / "data" / "ssl" / "key.pem"
    if cert_file.exists() and key_file.exists():
        def _run_https():
            try:
                srv = make_server(host, https_port, app, ssl_context=(str(cert_file), str(key_file)), threaded=True)
                srv.serve_forever()
            except Exception:
                pass

        threading.Thread(target=_run_https, daemon=True).start()

    app.run(host=host, port=port, debug=False, threaded=True)

