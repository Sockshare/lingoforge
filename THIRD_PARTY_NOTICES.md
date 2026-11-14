# Third-Party Notices

## Bundled Assets

1. **Nunito Font Family** (`static/fonts/nunito-*.woff2`)
   - Source: https://fonts.google.com/specimen/Nunito
   - Licence: SIL Open Font License 1.1

## Runtime Dependencies & External Services

- **Flask** (BSD-3-Clause) — HTTP server (`requirements.txt`).
- **edge-tts** (GPL-3.0, Python package, not bundled) — Synthesizes neural TTS audio on demand when internet connectivity is available; the browser falls back to `window.speechSynthesis` offline.
- **google-genai** (Apache-2.0, Python package, optional) — Used when `GEMINI_API_KEY` or `GOOGLE_API_KEY` is set; otherwise the engine uses built-in deterministic explanations and roleplay responses.
