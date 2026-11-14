#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path
from lingo_engine import LingoForgeEngine, levenshtein_distance
from curriculum_data import LANGUAGES, build_course_units, build_lesson_exercises


class TestLingoForgeEngine(unittest.TestCase):
    def test_languages_and_lifecycle(self):
        self.assertEqual(len(LANGUAGES), 11)
        self.assertIn("tl", LANGUAGES)
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "test.db"
            eng = LingoForgeEngine(db_path=db)
            state = eng.get_full_state()
            self.assertEqual(state["active_language"]["code"], "es")
            self.assertEqual(len(state["units"]), 8)
            res = eng.dispatch("SWITCH_LANGUAGE", {"lang_code": "tl"})
            self.assertTrue(res.get("ok"))
            self.assertEqual(eng.get_full_state()["active_language"]["code"], "tl")
            res = eng.dispatch("SWITCH_LANGUAGE", {"lang_code": "ja"})
            self.assertTrue(res.get("ok"))
            self.assertEqual(eng.get_full_state()["active_language"]["code"], "ja")
            exp = eng.explain_my_answer("es", "The coffee", "el agua", "el café")
            self.assertIn("headline", exp)
            rp = eng.roleplay_turn("es", "es_rp_cafe", "Hola, quiero un café por favor", [])
            self.assertIn("npc_reply", rp)

            # Verify completing a lesson increments crowns and marks completed=True on the map
            comp = eng.dispatch(
                "COMPLETE_LESSON",
                {"node_id": "ja_u1_n3", "xp_earned": 25, "accuracy": 100},
            )
            self.assertTrue(comp.get("ok"))
            self.assertGreaterEqual(comp.get("xp_awarded", 0), 25)
            u1_nodes = {n["id"]: n for n in comp["state"]["units"][0]["nodes"]}
            self.assertTrue(u1_nodes["ja_u1_n3"]["completed"])
            self.assertGreaterEqual(u1_nodes["ja_u1_n3"]["crowns"], 1)

    def test_all_40_lessons_unique_across_10_languages(self):
        for lang_code in LANGUAGES:
            units = build_course_units(lang_code)
            self.assertEqual(len(units), 8, f"{lang_code} should have 8 CEFR units")
            lesson_nodes = [
                n for u in units for n in u["nodes"] if n["type"] in ("lesson", "trophy")
            ]
            self.assertEqual(
                len(lesson_nodes), 40, f"{lang_code} should have 40 lessons"
            )
            seen_visual_answers = set()
            seen_sentences = set()
            for node in lesson_nodes:
                exs = build_lesson_exercises(lang_code, node["id"])
                self.assertEqual(len(exs), 7)
                self.assertNotIn("speaking", [e["type"] for e in exs])
                seen_visual_answers.add(exs[0]["answer"])
                seen_sentences.add(exs[6]["answer"])
            self.assertEqual(
                len(seen_visual_answers),
                40,
                f"{lang_code} should have 40 distinct vocabulary targets",
            )
            self.assertEqual(
                len(seen_sentences),
                40,
                f"{lang_code} should have 40 distinct target sentences",
            )

    def test_levenshtein(self):
        self.assertEqual(levenshtein_distance("cafe", "cafe"), 0)
        self.assertEqual(levenshtein_distance("cafe", "café"), 1)


if __name__ == "__main__":
    unittest.main()

