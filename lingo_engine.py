"""
LingoForge // Core Gamification, Half-Life Regression SRS, Levenshtein Grader & Duolingo Max AI Engine
"""

import json
import math
import os
import re
import sqlite3
import time
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional

from curriculum_data import (
    LANGUAGES,
    LANGUAGE_PACKS,
    SHOP_ITEMS,
    build_course_units,
    build_lesson_exercises,
    build_roleplay_scenarios,
    build_stories,
    get_alphabet_for_language,
)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "lingoforge.db"


def _strip_accents(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


def _normalize_text(text: str, strip_diacritics: bool = False) -> str:
    cleaned = text.strip().lower()
    cleaned = re.sub(r"[.,!?;:¿¡\"'«»()\[\]。、！？]", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    if strip_diacritics:
        cleaned = _strip_accents(cleaned)
    return cleaned


def levenshtein_distance(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[j - 1] + 1, prev[j] + 1, prev[j - 1] + cost))
        prev = curr
    return prev[-1]


def _resolve_gemini_api_key() -> Optional[str]:
    for env_var in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        val = os.environ.get(env_var)
        if val and val.strip():
            return val.strip()

    env_file = BASE_DIR / ".env"
    if env_file.exists():
        try:
            for line in env_file.read_text().splitlines():
                if line.startswith("GEMINI_API_KEY=") or line.startswith("GOOGLE_API_KEY="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
        except Exception:
            pass
    return None


class LingoForgeEngine:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.api_key = _resolve_gemini_api_key()
        self._init_db()

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._conn() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS user_profile (
                    id INTEGER PRIMARY KEY CHECK (id = 1),
                    username TEXT DEFAULT 'Morrisette',
                    avatar TEXT DEFAULT '🦉',
                    active_lang TEXT DEFAULT 'es',
                    xp INTEGER DEFAULT 1420,
                    daily_xp INTEGER DEFAULT 35,
                    daily_goal INTEGER DEFAULT 50,
                    streak INTEGER DEFAULT 14,
                    gems INTEGER DEFAULT 840,
                    hearts INTEGER DEFAULT 5,
                    max_hearts INTEGER DEFAULT 5,
                    unlimited_hearts INTEGER DEFAULT 1,
                    xp_boost_active INTEGER DEFAULT 0,
                    streak_freezes INTEGER DEFAULT 2,
                    league_name TEXT DEFAULT 'Diamond League',
                    lessons_completed INTEGER DEFAULT 18
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS node_progress (
                    node_id TEXT PRIMARY KEY,
                    lang_code TEXT,
                    crowns INTEGER DEFAULT 0,
                    completed INTEGER DEFAULT 0
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS srs_words (
                    word_id TEXT PRIMARY KEY,
                    lang_code TEXT,
                    word TEXT,
                    translation TEXT,
                    pos TEXT,
                    half_life_hours REAL DEFAULT 24.0,
                    last_practiced_ts REAL,
                    correct_count INTEGER DEFAULT 1,
                    wrong_count INTEGER DEFAULT 0
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS mistakes_inbox (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lang_code TEXT,
                    prompt TEXT,
                    user_answer TEXT,
                    correct_answer TEXT,
                    explanation TEXT,
                    created_ts REAL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS custom_units (
                    id TEXT PRIMARY KEY,
                    lang_code TEXT,
                    topic TEXT,
                    unit_json TEXT,
                    created_ts REAL
                )
                """
            )

            row = conn.execute("SELECT id FROM user_profile WHERE id = 1").fetchone()
            if not row:
                conn.execute("INSERT INTO user_profile (id) VALUES (1)")
                # Seed initial node progress for Spanish Unit 1 so tree looks alive
                conn.execute(
                    "INSERT OR IGNORE INTO node_progress (node_id, lang_code, crowns, completed) VALUES (?, ?, ?, ?)",
                    ("es_u1_n1", "es", 3, 1),
                )
                conn.execute(
                    "INSERT OR IGNORE INTO node_progress (node_id, lang_code, crowns, completed) VALUES (?, ?, ?, ?)",
                    ("es_u1_n2", "es", 2, 1),
                )

            # Seed SRS vocabulary for all languages
            now = time.time()
            for lcode, pack in LANGUAGE_PACKS.items():
                for idx, v in enumerate(pack["vocab"]):
                    # Vary initial last_practiced_ts so some words show as needing review
                    offset_hours = (idx * 7) % 30
                    hl = 24.0 if idx % 3 != 0 else 10.0
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO srs_words
                        (word_id, lang_code, word, translation, pos, half_life_hours, last_practiced_ts, correct_count, wrong_count)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            v["id"],
                            lcode,
                            v["word"],
                            v["translation"],
                            v["pos"],
                            hl,
                            now - offset_hours * 3600.0,
                            3 if idx % 2 == 0 else 1,
                            1 if idx % 3 == 0 else 0,
                        ),
                    )

            # Seed one sample mistake if empty so Mistakes Inbox is immediately demonstrable
            m_count = conn.execute("SELECT COUNT(*) AS c FROM mistakes_inbox").fetchone()["c"]
            if m_count == 0:
                conn.execute(
                    """
                    INSERT INTO mistakes_inbox (lang_code, prompt, user_answer, correct_answer, explanation, created_ts)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "es",
                        "Excuse me, where is the train station?",
                        "Disculpe, ¿dónde es la estación de tren?",
                        "Disculpe, ¿dónde está la estación de tren?",
                        "Use 'está' (estar) rather than 'es' (ser) when asking for the physical location of a building or place.",
                        now - 1800,
                    ),
                )
            conn.commit()

    def _compute_memory_strength(self, half_life_hours: float, last_practiced_ts: float) -> int:
        elapsed_hours = max(0.0, (time.time() - last_practiced_ts) / 3600.0)
        p_recall = math.pow(2.0, -elapsed_hours / max(1.0, half_life_hours))
        return max(12, min(100, int(round(p_recall * 100))))

    def get_full_state(self) -> Dict[str, Any]:
        with self._conn() as conn:
            prof = dict(conn.execute("SELECT * FROM user_profile WHERE id = 1").fetchone())
            lang_code = prof["active_lang"]
            if lang_code not in LANGUAGES:
                lang_code = "es"

            # Node progress map
            prog_rows = conn.execute(
                "SELECT node_id, crowns, completed FROM node_progress WHERE lang_code = ?",
                (lang_code,),
            ).fetchall()
            prog_map = {r["node_id"]: {"crowns": r["crowns"], "completed": bool(r["completed"])} for r in prog_rows}

            units = build_course_units(lang_code)
            # Append any AI custom units for this language
            custom_rows = conn.execute(
                "SELECT unit_json FROM custom_units WHERE lang_code = ? ORDER BY created_ts DESC",
                (lang_code,),
            ).fetchall()
            for crow in custom_rows:
                try:
                    c_unit = json.loads(crow["unit_json"])
                    units.append(c_unit)
                except Exception:
                    pass

            # Annotate nodes with crowns & unlock status
            prev_completed = True
            for u in units:
                for idx, node in enumerate(u["nodes"]):
                    nid = node["id"]
                    p = prog_map.get(nid, {"crowns": 0, "completed": False})
                    node["crowns"] = p["crowns"]
                    node["completed"] = p["completed"]
                    if idx == 0 or prev_completed or p["completed"]:
                        node["status"] = "completed" if p["completed"] else "active"
                    else:
                        node["status"] = "unlocked"
                    prev_completed = p["completed"]

            # SRS Words for active language
            srs_rows = conn.execute(
                "SELECT * FROM srs_words WHERE lang_code = ?",
                (lang_code,),
            ).fetchall()
            srs_list = []
            for r in srs_rows:
                strength = self._compute_memory_strength(r["half_life_hours"], r["last_practiced_ts"])
                srs_list.append(
                    {
                        "word_id": r["word_id"],
                        "word": r["word"],
                        "translation": r["translation"],
                        "pos": r["pos"],
                        "half_life_hours": round(r["half_life_hours"], 1),
                        "strength": strength,
                        "correct_count": r["correct_count"],
                        "wrong_count": r["wrong_count"],
                        "status": "Mastered" if strength >= 82 else ("Review Soon" if strength >= 55 else "Weak (Practice Now)"),
                    }
                )
            srs_list.sort(key=lambda x: x["strength"])

            # Mistakes inbox
            mistake_rows = conn.execute(
                "SELECT * FROM mistakes_inbox WHERE lang_code = ? ORDER BY created_ts DESC LIMIT 20",
                (lang_code,),
            ).fetchall()
            mistakes = [dict(m) for m in mistake_rows]

            # Daily Quests
            quests = [
                {
                    "id": "quest_xp",
                    "title": f"Earn {prof['daily_goal']} XP today",
                    "current": min(prof["daily_xp"], prof["daily_goal"]),
                    "target": prof["daily_goal"],
                    "reward_gems": 25,
                    "icon": "⚡",
                    "completed": prof["daily_xp"] >= prof["daily_goal"],
                },
                {
                    "id": "quest_lessons",
                    "title": "Complete 2 high-accuracy lessons or stories",
                    "current": min(2, prof["lessons_completed"] % 3 if prof["daily_xp"] > 0 else 1),
                    "target": 2,
                    "reward_gems": 30,
                    "icon": "🎯",
                    "completed": prof["daily_xp"] >= 40,
                },
                {
                    "id": "quest_max_ai",
                    "title": "Use Duolingo Max AI (Roleplay or Explain My Answer)",
                    "current": 1 if prof["xp"] > 1420 else 0,
                    "target": 1,
                    "reward_gems": 40,
                    "icon": "👑",
                    "completed": prof["xp"] > 1420,
                },
            ]

            # Weekly Diamond League Leaderboard (12 learners)
            leaderboard = [
                {"name": "Sofia_Madrid", "avatar": "🦊", "xp": 1890, "country": "🇪🇸", "is_user": False},
                {"name": "Kenji_Tokyo", "avatar": "🐼", "xp": 1720, "country": "🇯🇵", "is_user": False},
                {"name": "Chloe_Paris", "avatar": "🦋", "xp": 1580, "country": "🇫🇷", "is_user": False},
                {"name": prof["username"] + " (You)", "avatar": prof["avatar"], "xp": prof["xp"], "country": LANGUAGES[lang_code]["flag"], "is_user": True},
                {"name": "Lukas_Berlin", "avatar": "🦅", "xp": 1390, "country": "🇩🇪", "is_user": False},
                {"name": "Giulia_Roma", "avatar": "🦁", "xp": 1280, "country": "🇮🇹", "is_user": False},
                {"name": "Minho_Seoul", "avatar": "🐯", "xp": 1190, "country": "🇰🇷", "is_user": False},
                {"name": "Mateus_Rio", "avatar": "🦜", "xp": 1050, "country": "🇧🇷", "is_user": False},
                {"name": "Mei_Beijing", "avatar": "🐉", "xp": 940, "country": "🇨🇳", "is_user": False},
                {"name": "Amina_Riyadh", "avatar": "🐪", "xp": 830, "country": "🇸🇦", "is_user": False},
            ]
            leaderboard.sort(key=lambda r: r["xp"], reverse=True)
            for rank_idx, entry in enumerate(leaderboard, 1):
                entry["rank"] = rank_idx
                entry["zone"] = "promotion" if rank_idx <= 5 else ("demotion" if rank_idx >= 9 else "safe")

            return {
                "profile": {
                    **prof,
                    "unlimited_hearts": bool(prof["unlimited_hearts"]),
                    "xp_boost_active": bool(prof["xp_boost_active"]),
                },
                "active_language": LANGUAGES[lang_code],
                "languages": list(LANGUAGES.values()),
                "units": units,
                "stories": build_stories(lang_code),
                "roleplays": build_roleplay_scenarios(lang_code),
                "alphabet": get_alphabet_for_language(lang_code),
                "srs_words": srs_list,
                "mistakes": mistakes,
                "quests": quests,
                "leaderboard": leaderboard,
                "shop_items": SHOP_ITEMS,
                "ai_online": bool(self.api_key),
            }

    def grade_exercise_submission(
        self,
        lang_code: str,
        exercise: Dict[str, Any],
        user_answer: str,
    ) -> Dict[str, Any]:
        """Grades an exercise answer using exact match, accent check, or Levenshtein typo tolerance."""
        expected = str(exercise.get("answer", "")).strip()
        accepted_list = exercise.get("accepted_answers") or [expected]
        user_raw = str(user_answer or "").strip()

        if exercise.get("type") == "match_pairs" and user_raw == "ALL_MATCHED":
            self._update_srs(exercise.get("target_word_id"), correct=True)
            return {
                "correct": True,
                "status": "exact",
                "feedback": "Match Madness cleared! +Combo bonus!",
                "correct_answer": expected,
                "explanation": exercise.get("explanation", ""),
            }

        norm_user = _normalize_text(user_raw, strip_diacritics=False)
        norm_user_no_acc = _normalize_text(user_raw, strip_diacritics=True)

        for cand in accepted_list:
            norm_cand = _normalize_text(cand, strip_diacritics=False)
            norm_cand_no_acc = _normalize_text(cand, strip_diacritics=True)

            if norm_user == norm_cand:
                self._update_srs(exercise.get("target_word_id"), correct=True)
                return {
                    "correct": True,
                    "status": "exact",
                    "feedback": "Awesome! Spot on!",
                    "correct_answer": expected,
                    "explanation": exercise.get("explanation", ""),
                }

            if norm_user_no_acc == norm_cand_no_acc and len(norm_user_no_acc) > 0:
                self._update_srs(exercise.get("target_word_id"), correct=True)
                return {
                    "correct": True,
                    "status": "accent_warning",
                    "feedback": f"Great job! Pay attention to the accents: “{expected}”",
                    "correct_answer": expected,
                    "explanation": exercise.get("explanation", ""),
                }

            dist = levenshtein_distance(norm_user_no_acc, norm_cand_no_acc)
            if len(norm_cand_no_acc) >= 8 and dist == 1:
                self._update_srs(exercise.get("target_word_id"), correct=True)
                return {
                    "correct": True,
                    "status": "typo_accepted",
                    "feedback": f"Almost! You have a small typo. Correct spelling: “{expected}”",
                    "correct_answer": expected,
                    "explanation": exercise.get("explanation", ""),
                }

        # Wrong answer: deduct heart if not unlimited, update SRS & log mistake
        self._update_srs(exercise.get("target_word_id"), correct=False)
        with self._conn() as conn:
            prof = conn.execute("SELECT hearts, unlimited_hearts FROM user_profile WHERE id = 1").fetchone()
            new_hearts = prof["hearts"]
            if not prof["unlimited_hearts"] and new_hearts > 0:
                new_hearts -= 1
                conn.execute("UPDATE user_profile SET hearts = ? WHERE id = 1", (new_hearts,))
            conn.execute(
                """
                INSERT INTO mistakes_inbox (lang_code, prompt, user_answer, correct_answer, explanation, created_ts)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    lang_code,
                    exercise.get("source_text") or exercise.get("prompt") or "Exercise",
                    user_raw or "(empty)",
                    expected,
                    exercise.get("explanation", ""),
                    time.time(),
                ),
            )
            conn.commit()

        return {
            "correct": False,
            "status": "wrong",
            "feedback": f"Correct solution: “{expected}”",
            "correct_answer": expected,
            "explanation": exercise.get("explanation", ""),
        }

    def _update_srs(self, word_id: Optional[str], correct: bool) -> None:
        if not word_id:
            return
        now = time.time()
        with self._conn() as conn:
            row = conn.execute("SELECT * FROM srs_words WHERE word_id = ?", (word_id,)).fetchone()
            if not row:
                return
            hl = float(row["half_life_hours"])
            if correct:
                new_hl = min(720.0, hl * 2.0)
                conn.execute(
                    """
                    UPDATE srs_words
                    SET half_life_hours = ?, last_practiced_ts = ?, correct_count = correct_count + 1
                    WHERE word_id = ?
                    """,
                    (new_hl, now, word_id),
                )
            else:
                new_hl = max(2.0, hl * 0.5)
                conn.execute(
                    """
                    UPDATE srs_words
                    SET half_life_hours = ?, last_practiced_ts = ?, wrong_count = wrong_count + 1
                    WHERE word_id = ?
                    """,
                    (new_hl, now - 3600.0, word_id),
                )
            conn.commit()

    def dispatch(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = (action or "").upper().strip()

        if action == "SWITCH_LANGUAGE":
            lang_code = payload.get("lang_code", "es")
            if lang_code not in LANGUAGES:
                return {"ok": False, "error": f"Unsupported language: {lang_code}"}
            with self._conn() as conn:
                conn.execute("UPDATE user_profile SET active_lang = ? WHERE id = 1", (lang_code,))
                conn.commit()
            return {"ok": True, "message": f"Switched course to {LANGUAGES[lang_code]['name']}", "state": self.get_full_state()}

        if action == "START_LESSON":
            node_id = payload.get("node_id", "es_u1_n1")
            with self._conn() as conn:
                lang_code = payload.get("lang_code") or conn.execute("SELECT active_lang FROM user_profile WHERE id = 1").fetchone()["active_lang"]
            exercises = build_lesson_exercises(lang_code, node_id)
            return {"ok": True, "node_id": node_id, "lang_code": lang_code, "exercises": exercises}

        if action == "CHECK_EXERCISE":
            lang_code = payload.get("lang_code", "es")
            exercise = payload.get("exercise", {})
            user_answer = payload.get("user_answer", "")
            result = self.grade_exercise_submission(lang_code, exercise, user_answer)
            return {"ok": True, "result": result, "state": self.get_full_state()}

        if action == "COMPLETE_LESSON":
            node_id = payload.get("node_id", "es_u1_n1")
            base_xp = int(payload.get("xp_earned", 25))
            accuracy = int(payload.get("accuracy", 100))
            with self._conn() as conn:
                prof = conn.execute("SELECT * FROM user_profile WHERE id = 1").fetchone()
                lang_code = prof["active_lang"]
                multiplier = 2 if prof["xp_boost_active"] else 1
                combo_bonus = 5 if accuracy >= 90 else 0
                total_xp = (base_xp + combo_bonus) * multiplier
                gems_earned = 15 if accuracy >= 90 else 10

                conn.execute(
                    """
                    UPDATE user_profile
                    SET xp = xp + ?,
                        daily_xp = daily_xp + ?,
                        gems = gems + ?,
                        lessons_completed = lessons_completed + 1,
                        hearts = CASE WHEN ? = 'practice' THEN MIN(max_hearts, hearts + 1) ELSE hearts END
                    WHERE id = 1
                    """,
                    (total_xp, total_xp, gems_earned, "practice" if "practice" in node_id else "lesson"),
                )

                existing = conn.execute(
                    "SELECT crowns FROM node_progress WHERE node_id = ?", (node_id,)
                ).fetchone()
                new_crowns = min(5, (existing["crowns"] + 1) if existing else 1)
                conn.execute(
                    """
                    INSERT INTO node_progress (node_id, lang_code, crowns, completed)
                    VALUES (?, ?, ?, 1)
                    ON CONFLICT(node_id) DO UPDATE SET crowns = ?, completed = 1
                    """,
                    (node_id, lang_code, new_crowns, new_crowns),
                )
                conn.commit()
            return {
                "ok": True,
                "xp_awarded": total_xp,
                "gems_awarded": gems_earned,
                "crowns": new_crowns,
                "state": self.get_full_state(),
            }

        if action == "COMPLETE_STORY":
            story_id = payload.get("story_id", "es_story_cafe")
            xp_reward = int(payload.get("xp_reward", 30))
            gems_reward = int(payload.get("gems_reward", 15))
            with self._conn() as conn:
                prof = conn.execute("SELECT * FROM user_profile WHERE id = 1").fetchone()
                multiplier = 2 if prof["xp_boost_active"] else 1
                awarded_xp = xp_reward * multiplier
                conn.execute(
                    """
                    UPDATE user_profile
                    SET xp = xp + ?, daily_xp = daily_xp + ?, gems = gems + ?, lessons_completed = lessons_completed + 1
                    WHERE id = 1
                    """,
                    (awarded_xp, awarded_xp, gems_reward),
                )
                conn.commit()
            return {"ok": True, "story_id": story_id, "xp_awarded": awarded_xp, "gems_awarded": gems_reward, "state": self.get_full_state()}

        if action == "PRACTICE_WEAK_WORDS":
            with self._conn() as conn:
                prof = conn.execute("SELECT active_lang, max_hearts, hearts FROM user_profile WHERE id = 1").fetchone()
                lang_code = prof["active_lang"]
                now = time.time()
                conn.execute(
                    """
                    UPDATE srs_words
                    SET half_life_hours = MIN(720.0, half_life_hours * 1.8),
                        last_practiced_ts = ?,
                        correct_count = correct_count + 1
                    WHERE lang_code = ?
                    """,
                    (now, lang_code),
                )
                conn.execute(
                    """
                    UPDATE user_profile
                    SET xp = xp + 20, daily_xp = daily_xp + 20, hearts = MIN(max_hearts, hearts + 1)
                    WHERE id = 1
                    """
                )
                conn.commit()
            return {"ok": True, "message": "Restored SRS memory strength and earned +1 Heart & +20 XP!", "state": self.get_full_state()}

        if action == "CLEAR_MISTAKE":
            mistake_id = payload.get("mistake_id")
            with self._conn() as conn:
                if mistake_id:
                    conn.execute("DELETE FROM mistakes_inbox WHERE id = ?", (mistake_id,))
                else:
                    conn.execute("DELETE FROM mistakes_inbox")
                conn.execute("UPDATE user_profile SET xp = xp + 10, daily_xp = daily_xp + 10 WHERE id = 1")
                conn.commit()
            return {"ok": True, "state": self.get_full_state()}

        if action == "BUY_ITEM":
            item_id = payload.get("item_id")
            item = next((i for i in SHOP_ITEMS if i["id"] == item_id), None)
            if not item:
                return {"ok": False, "error": "Unknown shop item"}
            with self._conn() as conn:
                prof = conn.execute("SELECT * FROM user_profile WHERE id = 1").fetchone()
                if prof["gems"] < item["cost"]:
                    return {"ok": False, "error": "Not enough Gems!"}
                new_gems = prof["gems"] - item["cost"]
                if item_id == "heart_refill":
                    conn.execute("UPDATE user_profile SET gems = ?, hearts = max_hearts WHERE id = 1", (new_gems,))
                elif item_id == "streak_freeze":
                    conn.execute("UPDATE user_profile SET gems = ?, streak_freezes = MIN(2, streak_freezes + 1) WHERE id = 1", (new_gems,))
                elif item_id == "xp_boost_15m":
                    conn.execute("UPDATE user_profile SET gems = ?, xp_boost_active = 1 WHERE id = 1", (new_gems,))
                elif item_id == "duolingo_max_pass":
                    conn.execute("UPDATE user_profile SET gems = ?, unlimited_hearts = 1, hearts = max_hearts WHERE id = 1", (new_gems,))
                conn.commit()
            return {"ok": True, "item": item, "state": self.get_full_state()}

        if action == "TOGGLE_UNLIMITED_HEARTS":
            with self._conn() as conn:
                prof = conn.execute("SELECT unlimited_hearts FROM user_profile WHERE id = 1").fetchone()
                new_val = 0 if prof["unlimited_hearts"] else 1
                conn.execute(
                    "UPDATE user_profile SET unlimited_hearts = ?, hearts = max_hearts WHERE id = 1",
                    (new_val,),
                )
                conn.commit()
            return {"ok": True, "state": self.get_full_state()}

        return {"ok": False, "error": f"Unknown action: {action}"}

    # ------------------------------------------------------------------
    # Duolingo Max AI Features (Powered by Gemini + Deterministic Fallback)
    # ------------------------------------------------------------------
    def explain_my_answer(
        self,
        lang_code: str,
        prompt: str,
        user_answer: str,
        correct_answer: str,
        base_explanation: str = "",
    ) -> Dict[str, Any]:
        lang = LANGUAGES.get(lang_code, LANGUAGES["es"])

        if self.api_key:
            try:
                from google import genai

                client = genai.Client(api_key=self.api_key)
                sys_prompt = (
                    f"You are Duo (Duolingo Max 'Explain My Answer' AI Tutor) for {lang['name']}. "
                    f"Return a concise JSON object with keys: "
                    f"headline (string), grammar_rule (string), word_breakdown (array of {{token, meaning, role}}), pro_tip (string). "
                    f"Exercise prompt: {prompt}\nLearner answered: {user_answer}\nCorrect solution: {correct_answer}\nContext: {base_explanation}"
                )
                resp = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=sys_prompt,
                    config={"response_mime_type": "application/json"},
                )
                if resp and resp.text:
                    parsed = json.loads(resp.text)
                    parsed["source"] = "Duolingo Max Gemini AI"
                    return parsed
            except Exception:
                pass

        # Deterministic Linguistic Breakdown Fallback
        tokens = correct_answer.split()
        pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
        gloss_map: Dict[str, str] = {}
        for s in pack["sentences"]:
            gloss_map.update(s.get("gloss", {}))

        breakdown = []
        for t in tokens[:8]:
            breakdown.append(
                {
                    "token": t,
                    "meaning": gloss_map.get(t, gloss_map.get(t.rstrip(".,?!"), "core phrase token")),
                    "role": "Verb / Core" if any(v in t.lower() for v in ("quiero", "está", "cuesta", "voudrais", "möchte", "ください", "주세요")) else "Lexical / Particle",
                }
            )

        is_match = _normalize_text(user_answer, True) == _normalize_text(correct_answer, True)
        return {
            "source": "Duolingo Max AI Linguistic Engine",
            "headline": (
                f"Why “{correct_answer}” works in {lang['name']}"
                if is_match
                else f"Comparing “{user_answer or '(blank)'}” vs. “{correct_answer}”"
            ),
            "grammar_rule": base_explanation
            or f"In {lang['name']}, notice the word order, polite register, and grammatical agreement in “{correct_answer}”.",
            "word_breakdown": breakdown,
            "pro_tip": f"Read “{correct_answer}” aloud right after clicking the 🐢 slow-audio button to lock the rhythm into muscle memory!",
        }

    def roleplay_turn(
        self,
        lang_code: str,
        scenario_id: str,
        user_message: str,
        history: List[Dict[str, str]],
    ) -> Dict[str, Any]:
        lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
        scenarios = build_roleplay_scenarios(lang_code)
        scenario = next((s for s in scenarios if s["id"] == scenario_id), scenarios[0])

        # Award XP for active roleplay participation
        with self._conn() as conn:
            conn.execute("UPDATE user_profile SET xp = xp + 15, daily_xp = daily_xp + 15 WHERE id = 1")
            conn.commit()

        if self.api_key:
            try:
                from google import genai

                client = genai.Client(api_key=self.api_key)
                prompt = (
                    f"You are playing the role of {scenario['npc_name']} in a Duolingo Max AI Roleplay for a learner studying {lang['name']}. "
                    f"Scenario: {scenario['title']} ({scenario['objective']}). "
                    f"Learner said: {user_message}\n"
                    f"Respond with JSON: {{'npc_reply': '<natural reply in {lang['name']}>', 'npc_reply_en': '<English translation>', "
                    f"'coaching_tip': '<1-sentence friendly grammar/vocabulary feedback on what the learner said>', "
                    f"'cefr_score': {{'fluency': 94, 'grammar': 92, 'register': 'Polite A1/A2'}}}}"
                )
                resp = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config={"response_mime_type": "application/json"},
                )
                if resp and resp.text:
                    data = json.loads(resp.text)
                    data["xp_awarded"] = 15
                    data["state"] = self.get_full_state()
                    return data
            except Exception:
                pass

        # Rich deterministic multi-turn roleplay response per language
        turn_count = len(history)
        pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
        v0 = pack["vocab"][0]
        v1 = pack["vocab"][1]

        if lang_code == "es":
            replies = [
                (
                    "¡Excelente elección! Un café con leche recién hecho y pan caliente. ¿Desea tomarlo aquí en la terraza o para llevar?",
                    "Excellent choice! A freshly made coffee with milk and warm bread. Would you like to have it here on the terrace or to go?",
                ),
                (
                    "¡Perfecto! Son cuatro euros con cincuenta céntimos, por favor. ¡Que tenga un día maravilloso en Madrid!",
                    "Perfect! That is four euros and fifty cents, please. Have a wonderful day in Madrid!",
                ),
            ]
        elif lang_code == "fr":
            replies = [
                (
                    "Très bien ! Un café bien chaud et un croissant au beurre. Vous désirez autre chose ?",
                    "Very good! A piping hot coffee and a butter croissant. Would you like anything else?",
                ),
                (
                    "Parfait ! Cela fait quatre euros, s'il vous plaît. Bonne journée à Paris !",
                    "Perfect! That makes four euros, please. Have a great day in Paris!",
                ),
            ]
        elif lang_code == "ja":
            replies = [
                (
                    "かしこまりました！あたたかいコーヒーとおみずですね。店内（てんない）でお召し上がりですか？",
                    "Certainly! Hot coffee and water. Will you be dining in the café?",
                ),
                (
                    "ありがとうございます！合計（ごうけい）は五百円（500円）になります。どうぞごゆっくり！",
                    "Thank you very much! The total is 500 yen. Please enjoy!",
                ),
            ]
        else:
            replies = [
                (
                    f"¡Excelente! {v0['word']} + {v1['word']}!",
                    f"Wonderful! Coming right up: {v0['translation']} and {v1['translation']}. Anything else today?",
                ),
                (
                    pack["sentences"][-1]["target"],
                    "Thank you very much! Your pronunciation and politeness were spot on!",
                ),
            ]

        chosen_native, chosen_en = replies[turn_count % len(replies)]
        return {
            "npc_reply": chosen_native,
            "npc_reply_en": chosen_en,
            "coaching_tip": f"Great phrasing! Your use of “{user_message}” fits natural {lang['name']} polite register.",
            "cefr_score": {
                "fluency": min(99, 88 + turn_count * 4),
                "grammar": 94,
                "register": "Polite Native-Like (CEFR A2)",
            },
            "xp_awarded": 15,
            "state": self.get_full_state(),
        }

    def generate_custom_unit(self, lang_code: str, topic: str) -> Dict[str, Any]:
        lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
        clean_topic = (topic or "Street Food & Nightlife").strip()
        unit_id = f"{lang_code}_custom_{int(time.time())}"

        new_unit = {
            "unit_number": 4,
            "id": unit_id,
            "section": "Duolingo Max Custom AI Curriculum",
            "title": f"AI Custom Unit: {clean_topic}",
            "subtitle": f"Personalized {lang['name']} vocabulary, listening & roleplay generated for “{clean_topic}”.",
            "color": "#ff9600",
            "border_color": "#cc7800",
            "guidebook": {
                "title": f"AI Guidebook: {clean_topic} ({lang['name']})",
                "summary": f"Custom-tailored {lang['name']} expressions and cultural tips for {clean_topic}.",
                "grammar_tip": f"Combine polite modal verbs with topic-specific nouns when discussing {clean_topic}.",
                "cultural_note": f"Local speakers appreciate when travelers use authentic terms for {clean_topic}.",
                "key_phrases": [
                    {"native": LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])["sentences"][0]["target"], "english": f"Core phrase for {clean_topic}"},
                ],
            },
            "nodes": [
                {
                    "id": f"{unit_id}_n1",
                    "type": "lesson",
                    "title": f"{clean_topic[:18]} Basics",
                    "subtitle": "AI-Curated Vocabulary & Audio",
                    "icon": "star",
                    "offset_x": -35,
                    "max_crowns": 5,
                    "xp_reward": 30,
                },
                {
                    "id": f"{unit_id}_roleplay",
                    "type": "roleplay",
                    "scenario_id": f"{lang_code}_rp_cafe",
                    "title": f"MAX Roleplay: {clean_topic[:16]}",
                    "subtitle": "Live AI Conversation Mission",
                    "icon": "max",
                    "offset_x": 35,
                    "max_crowns": 1,
                    "xp_reward": 45,
                },
            ],
        }

        with self._conn() as conn:
            conn.execute(
                "INSERT INTO custom_units (id, lang_code, topic, unit_json, created_ts) VALUES (?, ?, ?, ?, ?)",
                (unit_id, lang_code, clean_topic, json.dumps(new_unit), time.time()),
            )
            conn.execute("UPDATE user_profile SET xp = xp + 25, daily_xp = daily_xp + 25 WHERE id = 1")
            conn.commit()

        return {"ok": True, "unit": new_unit, "state": self.get_full_state()}
