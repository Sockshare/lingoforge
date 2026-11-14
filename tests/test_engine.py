#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path
from lingo_engine import LingoForgeEngine, levenshtein_distance
from curriculum_data import LANGUAGES


class TestLingoForgeEngine(unittest.TestCase):
    def test_languages_and_lifecycle(self):
        self.assertEqual(len(LANGUAGES), 10)
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "test.db"
            eng = LingoForgeEngine(db_path=db)
            state = eng.get_full_state()
            self.assertEqual(state["active_language"]["code"], "es")
            self.assertGreaterEqual(len(state["units"]), 3)
            res = eng.dispatch("SWITCH_LANGUAGE", {"lang_code": "ja"})
            self.assertTrue(res.get("ok"))
            self.assertEqual(eng.get_full_state()["active_language"]["code"], "ja")
            exp = eng.explain_my_answer("es", "The coffee", "el agua", "el café")
            self.assertIn("headline", exp)
            rp = eng.roleplay_turn("es", "es_rp_cafe", "Hola, quiero un café por favor", [])
            self.assertIn("npc_reply", rp)

    def test_levenshtein(self):
        self.assertEqual(levenshtein_distance("cafe", "cafe"), 0)
        self.assertEqual(levenshtein_distance("cafe", "café"), 1)


if __name__ == "__main__":
    unittest.main()
