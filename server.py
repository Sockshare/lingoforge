"""
LingoForge // Standalone Duolingo & Duolingo Max Flask Server (Port 8103)
Provides REST APIs, SQLite state persistence, Duolingo Max AI endpoints, and Neural Edge-TTS Audio.
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
    return jsonify({"status": "ok", "app": "LingoForge // Duolingo & Duolingo Max", "port": 8103})


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
        except Exception as exc:
            return jsonify({"ok": False, "fallback_browser_tts": True, "reason": str(exc)}), 200

    if cached_mp3.exists() and cached_mp3.stat().st_size > 0:
        return send_file(str(cached_mp3), mimetype="audio/mpeg")

    return jsonify({"ok": False, "fallback_browser_tts": True}), 200


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8103))
    app.run(host=host, port=port, debug=False)
