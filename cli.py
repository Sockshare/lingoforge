#!/usr/bin/env python3
"""
LingoForge // 1:1 CLI Parity Tool
Allows inspecting state, switching languages, grading answers, running Duolingo Max AI, and testing SRS from the terminal.
"""

import argparse
import json
from lingo_engine import LingoForgeEngine


def main():
    parser = argparse.ArgumentParser(description="LingoForge Duolingo & Duolingo Max CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("state", help="Print current profile, course units, SRS words, and leaderboard")

    p_lang = sub.add_parser("switch-lang", help="Switch active language course")
    p_lang.add_argument("lang_code", help="Language code (es, fr, ja, de, it, ko, zh, pt, ru, ar)")

    p_explain = sub.add_parser("explain", help="Run Duolingo Max Explain My Answer")
    p_explain.add_argument("--lang", default="es")
    p_explain.add_argument("--prompt", required=True)
    p_explain.add_argument("--user", required=True)
    p_explain.add_argument("--correct", required=True)

    p_practice = sub.add_parser("practice-srs", help="Run SRS Weak Word restoration")

    args = parser.parse_args()
    eng = LingoForgeEngine()

    if args.cmd == "switch-lang":
        print(json.dumps(eng.dispatch("SWITCH_LANGUAGE", {"lang_code": args.lang_code}), indent=2, ensure_ascii=False))
    elif args.cmd == "explain":
        print(
            json.dumps(
                eng.explain_my_answer(args.lang, args.prompt, args.user, args.correct),
                indent=2,
                ensure_ascii=False,
            )
        )
    elif args.cmd == "practice-srs":
        print(json.dumps(eng.dispatch("PRACTICE_WEAK_WORDS", {}), indent=2, ensure_ascii=False))
    else:
        state = eng.get_full_state()
        summary = {
            "profile": state["profile"],
            "active_language": state["active_language"]["name"],
            "units_count": len(state["units"]),
            "srs_words_count": len(state["srs_words"]),
            "weakest_words": state["srs_words"][:3],
            "leaderboard_top3": state["leaderboard"][:3],
        }
        print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
