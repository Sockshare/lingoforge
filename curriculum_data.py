"""
LingoForge // Duolingo & Duolingo Max Curriculum, Stories, Roleplay & Alphabet Data
Supports 10 languages with CEFR-aligned Units, Guidebooks, 8 Exercise Mechanics,
Interactive Voiced Stories, Duolingo Max AI Roleplay Scenarios, and Character Trainers.
"""

from typing import Dict, Any, List

LANGUAGES: Dict[str, Dict[str, Any]] = {
    "es": {
        "code": "es",
        "name": "Spanish",
        "native_name": "Español",
        "flag": "🇪🇸",
        "learners": "48.2M",
        "cefr_range": "A1 – B2",
        "voice_female": "es-ES-ElviraNeural",
        "voice_male": "es-MX-JorgeNeural",
        "speech_lang": "es-ES",
        "accents": ["á", "é", "í", "ó", "ú", "ñ", "ü", "¿", "¡"],
        "script_name": "Spanish Phonetics & Accents",
        "tagline": "Order tapas in Madrid, travel across Latin America, and master Romance grammar.",
    },
    "fr": {
        "code": "fr",
        "name": "French",
        "native_name": "Français",
        "flag": "🇫🇷",
        "learners": "32.9M",
        "cefr_range": "A1 – B2",
        "voice_female": "fr-FR-DeniseNeural",
        "voice_male": "fr-FR-HenriNeural",
        "speech_lang": "fr-FR",
        "accents": ["é", "è", "ê", "ë", "à", "â", "ù", "û", "ç", "œ", "î", "ï"],
        "script_name": "French Liaisons & Accents",
        "tagline": "Chat in Parisian cafés, master nasal vowels, and read classic literature.",
    },
    "ja": {
        "code": "ja",
        "name": "Japanese",
        "native_name": "日本語",
        "flag": "🇯🇵",
        "learners": "24.6M",
        "cefr_range": "A1 – B1",
        "voice_female": "ja-JP-NanamiNeural",
        "voice_male": "ja-JP-KeitaNeural",
        "speech_lang": "ja-JP",
        "accents": ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "は", "を", "ん", "。"],
        "script_name": "Hiragana, Katakana & Kanji",
        "tagline": "Navigate Tokyo, read Hiragana & Katakana, and master polite desu/masu speech.",
    },
    "de": {
        "code": "de",
        "name": "German",
        "native_name": "Deutsch",
        "flag": "🇩🇪",
        "learners": "18.4M",
        "cefr_range": "A1 – B2",
        "voice_female": "de-DE-KatjaNeural",
        "voice_male": "de-DE-ConradNeural",
        "speech_lang": "de-DE",
        "accents": ["ä", "ö", "ü", "ß", "Ä", "Ö", "Ü"],
        "script_name": "Umlauts & Cases (Der/Die/Das)",
        "tagline": "Conquer grammatical cases, compound nouns, and everyday life in Berlin & Munich.",
    },
    "it": {
        "code": "it",
        "name": "Italian",
        "native_name": "Italiano",
        "flag": "🇮🇹",
        "learners": "14.8M",
        "cefr_range": "A1 – B1",
        "voice_female": "it-IT-ElsaNeural",
        "voice_male": "it-IT-DiegoNeural",
        "speech_lang": "it-IT",
        "accents": ["à", "è", "é", "ì", "ò", "ó", "ù"],
        "script_name": "Italian Double Consonants & Stress",
        "tagline": "Order espresso in Rome, explore Renaissance art, and speak with musical cadence.",
    },
    "ko": {
        "code": "ko",
        "name": "Korean",
        "native_name": "한국어",
        "flag": "🇰🇷",
        "learners": "17.1M",
        "cefr_range": "A1 – B1",
        "voice_female": "ko-KR-SunHiNeural",
        "voice_male": "ko-KR-InJoonNeural",
        "speech_lang": "ko-KR",
        "accents": ["안", "녕", "하", "세", "요", "감", "사", "합", "니", "다", "은", "는", "이", "가"],
        "script_name": "Hangul Syllables & Batchim",
        "tagline": "Read Hangul syllable blocks, understand K-drama honorifics, and explore Seoul.",
    },
    "zh": {
        "code": "zh",
        "name": "Mandarin",
        "native_name": "中文 (普通话)",
        "flag": "🇨🇳",
        "learners": "12.9M",
        "cefr_range": "A1 – B1",
        "voice_female": "zh-CN-XiaoxiaoNeural",
        "voice_male": "zh-CN-YunxiNeural",
        "speech_lang": "zh-CN",
        "accents": ["ā", "á", "ǎ", "à", "ē", "é", "ě", "è", "ī", "í", "ǐ", "ì", "ō", "ó", "ǒ", "ò", "ū", "ú", "ǔ", "ù"],
        "script_name": "Pinyin Tones & Hanzi Radicals",
        "tagline": "Master the 4 Mandarin tones, high-frequency Hanzi characters, and daily conversation.",
    },
    "pt": {
        "code": "pt",
        "name": "Portuguese",
        "native_name": "Português",
        "flag": "🇧🇷",
        "learners": "11.5M",
        "cefr_range": "A1 – B1",
        "voice_female": "pt-BR-FranciscaNeural",
        "voice_male": "pt-BR-AntonioNeural",
        "speech_lang": "pt-BR",
        "accents": ["á", "â", "ã", "à", "ç", "é", "ê", "í", "ó", "ô", "õ", "ú"],
        "script_name": "Nasal Diphthongs & Brazilian Cadence",
        "tagline": "Speak natural Brazilian Portuguese for Rio beaches, bossa nova, and business.",
    },
    "ru": {
        "code": "ru",
        "name": "Russian",
        "native_name": "Русский",
        "flag": "🇷🇺",
        "learners": "9.4M",
        "cefr_range": "A1 – B1",
        "voice_female": "ru-RU-SvetlanaNeural",
        "voice_male": "ru-RU-DmitryNeural",
        "speech_lang": "ru-RU",
        "accents": ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "э", "ю", "я"],
        "script_name": "Cyrillic Alphabet & Cases",
        "tagline": "Decode the 33-letter Cyrillic alphabet and master expressive Slavic grammar.",
    },
    "ar": {
        "code": "ar",
        "name": "Arabic",
        "native_name": "العربية",
        "flag": "🇸🇦",
        "learners": "8.7M",
        "cefr_range": "A1 – B1",
        "voice_female": "ar-SA-ZariyahNeural",
        "voice_male": "ar-SA-HamedNeural",
        "speech_lang": "ar-SA",
        "accents": ["ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ر", "س", "ش", "ص", "ع", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي", "ة", "ء"],
        "script_name": "Arabic Script & Connected Forms",
        "tagline": "Read right-to-left connected script, root patterns, and warm Middle Eastern greetings.",
    },
}


# Core vocabulary & phrase packs for each language so every language has authentic, native exercises
LANGUAGE_PACKS: Dict[str, Dict[str, Any]] = {
    "es": {
        "vocab": [
            {"id": "es_cafe", "word": "el café", "translation": "the coffee", "pos": "noun (m)", "gender": "masculine", "roman": "el ka-FE", "icon": "coffee", "unit": 1, "note": "Masculine singular noun using 'el'."},
            {"id": "es_agua", "word": "el agua", "translation": "the water", "pos": "noun (f)", "gender": "feminine (takes el)", "roman": "el A-gwa", "icon": "water", "unit": 1, "note": "Feminine noun that uses 'el' in singular to avoid double 'a' sound (el agua fría)."},
            {"id": "es_pan", "word": "el pan", "translation": "the bread", "pos": "noun (m)", "gender": "masculine", "roman": "el pan", "icon": "bread", "unit": 1, "note": "Common masculine food noun."},
            {"id": "es_leche", "word": "la leche", "translation": "the milk", "pos": "noun (f)", "gender": "feminine", "roman": "la LE-che", "icon": "milk", "unit": 1, "note": "Feminine singular noun using 'la'."},
            {"id": "es_hola", "word": "hola, buenos días", "translation": "hello, good morning", "pos": "phrase", "gender": "n/a", "roman": "O-la BWE-nos DEE-as", "icon": "sun", "unit": 1, "note": "Standard polite morning greeting."},
            {"id": "es_cuenta", "word": "la cuenta, por favor", "translation": "the bill, please", "pos": "phrase", "gender": "feminine", "roman": "la KWEN-ta por fa-VOR", "icon": "receipt", "unit": 1, "note": "Essential restaurant phrase."},
            {"id": "es_estacion", "word": "la estación de tren", "translation": "the train station", "pos": "noun (f)", "gender": "feminine", "roman": "la es-ta-SYON de tren", "icon": "train", "unit": 2, "note": "Nouns ending in -ción are always feminine."},
            {"id": "es_boleto", "word": "un boleto para Madrid", "translation": "a ticket to Madrid", "pos": "phrase", "gender": "masculine", "roman": "oon bo-LE-to PA-ra ma-DREED", "icon": "ticket", "unit": 2, "note": "'Para' indicates destination."},
            {"id": "es_hotel", "word": "el hotel está cerca", "translation": "the hotel is nearby", "pos": "sentence", "gender": "masculine", "roman": "el o-TEL es-TA SER-ka", "icon": "hotel", "unit": 2, "note": "Uses 'estar' (está) for physical location!"},
            {"id": "es_pasaporte", "word": "mi pasaporte está aquí", "translation": "my passport is here", "pos": "sentence", "gender": "masculine", "roman": "mee pa-sa-POR-te es-TA a-KEE", "icon": "passport", "unit": 2, "note": "Uses 'está' for location."},
            {"id": "es_manzana", "word": "la manzana roja", "translation": "the red apple", "pos": "noun (f)", "gender": "feminine", "roman": "la man-SA-na RO-ha", "icon": "apple", "unit": 3, "note": "Adjectives follow the noun and match gender (roja)."},
            {"id": "es_queso", "word": "el queso fresco", "translation": "the fresh cheese", "pos": "noun (m)", "gender": "masculine", "roman": "el KE-so FRES-ko", "icon": "cheese", "unit": 3, "note": "Adjective 'fresco' agrees with masculine 'queso'."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Yo quiero un café con leche, por favor.",
                "english": "I want a coffee with milk, please.",
                "tokens": ["Yo", "quiero", "un", "café", "con", "leche,", "por", "favor."],
                "distractors": ["agua", "somos", "la", "tienen"],
                "gloss": {"Yo": "I", "quiero": "want (querer, 1st sg)", "un": "a (masc)", "café": "coffee", "con": "with", "leche,": "milk", "por": "for / please", "favor.": "favor (please)"},
                "cloze_sentence": "Yo ___ un café con leche, por favor.",
                "cloze_answer": "quiero",
                "cloze_options": ["quiero", "queremos", "quiere", "quieren"],
                "grammar_tip": "'Querer' (to want) is a stem-changing verb (e → ie): yo quiero, tú quieres, él/ella quiere.",
                "dialogue_prompt": "¡Buenos días! ¿Qué desea tomar hoy?",
                "dialogue_prompt_en": "Good morning! What would you like to drink today?",
                "dialogue_options": [
                    "Yo quiero un café con leche, por favor.",
                    "La estación de tren está lejos.",
                    "Mi pasaporte es azul.",
                ],
            },
            {
                "unit": 1,
                "target": "¿Cuánto cuesta el pan y el queso?",
                "english": "How much do the bread and the cheese cost?",
                "tokens": ["¿Cuánto", "cuesta", "el", "pan", "y", "el", "queso?"],
                "distractors": ["dónde", "está", "la", "leche"],
                "gloss": {"¿Cuánto": "How much", "cuesta": "costs (costar)", "el": "the (masc)", "pan": "bread", "y": "and", "queso?": "cheese"},
                "cloze_sentence": "¿Cuánto ___ el pan y el queso?",
                "cloze_answer": "cuesta",
                "cloze_options": ["cuesta", "estoy", "hablo", "tengo"],
                "grammar_tip": "'¿Cuánto cuesta...?' asks the price of an item (costar: o → ue stem change).",
                "dialogue_prompt": "Aquí tiene el pan recién horneado. ¿Algo más?",
                "dialogue_prompt_en": "Here is the freshly baked bread. Anything else?",
                "dialogue_options": [
                    "¿Cuánto cuesta el pan y el queso?",
                    "Buenas noches, hasta mañana.",
                    "Yo vivo en Barcelona.",
                ],
            },
            {
                "unit": 2,
                "target": "Disculpe, ¿dónde está la estación de tren?",
                "english": "Excuse me, where is the train station?",
                "tokens": ["Disculpe,", "¿dónde", "está", "la", "estación", "de", "tren?"],
                "distractors": ["es", "son", "el", "boleto"],
                "gloss": {"Disculpe,": "Excuse me (formal)", "¿dónde": "where", "está": "is (location - estar)", "la": "the (fem)", "estación": "station", "de": "of", "tren?": "train"},
                "cloze_sentence": "Disculpe, ¿dónde ___ la estación de tren?",
                "cloze_answer": "está",
                "cloze_options": ["está", "es", "eres", "somos"],
                "grammar_tip": "Always use ESTAR (está) — never SER (es) — when asking for the physical location of a place or object!",
                "dialogue_prompt": "Necesito tomar el tren rápido a Madrid.",
                "dialogue_prompt_en": "I need to take the express train to Madrid.",
                "dialogue_options": [
                    "Disculpe, ¿dónde está la estación de tren?",
                    "Me gusta mucho la manzana roja.",
                    "El café está muy caliente.",
                ],
            },
            {
                "unit": 2,
                "target": "Nosotros necesitamos dos boletos para Madrid.",
                "english": "We need two tickets to Madrid.",
                "tokens": ["Nosotros", "necesitamos", "dos", "boletos", "para", "Madrid."],
                "distractors": ["necesito", "por", "un", "hotel"],
                "gloss": {"Nosotros": "We", "necesitamos": "need (-amos 1st pl)", "dos": "two", "boletos": "tickets", "para": "to / bound for", "Madrid.": "Madrid"},
                "cloze_sentence": "Nosotros ___ dos boletos para Madrid.",
                "cloze_answer": "necesitamos",
                "cloze_options": ["necesitamos", "necesito", "necesitan", "necesitas"],
                "grammar_tip": "For 'nosotros' (we), regular -ar verbs end in -amos (necesitar → necesitamos).",
                "dialogue_prompt": "Bienvenidos a la taquilla. ¿Adónde viajan hoy?",
                "dialogue_prompt_en": "Welcome to the ticket counter. Where are you traveling today?",
                "dialogue_options": [
                    "Nosotros necesitamos dos boletos para Madrid.",
                    "La leche está en el refrigerador.",
                    "Muchas gracias por la cena.",
                ],
            },
            {
                "unit": 3,
                "target": "La cuenta, por favor, todo estuvo delicioso.",
                "english": "The bill, please, everything was delicious.",
                "tokens": ["La", "cuenta,", "por", "favor,", "todo", "estuvo", "delicioso."],
                "distractors": ["el", "mesa", "estoy", "mañana"],
                "gloss": {"La": "The (fem)", "cuenta,": "bill / check", "por": "for", "favor,": "favor (please)", "todo": "everything", "estuvo": "was (preterite)", "delicioso.": "delicious"},
                "cloze_sentence": "La ___, por favor, todo estuvo delicioso.",
                "cloze_answer": "cuenta",
                "cloze_options": ["cuenta", "puerta", "maleta", "ventana"],
                "grammar_tip": "'Estuvo' is the preterite (completed past) of 'estar' used to react to a meal or event that just finished.",
                "dialogue_prompt": "¿Les gustó la paella y el postre?",
                "dialogue_prompt_en": "Did you enjoy the paella and the dessert?",
                "dialogue_options": [
                    "La cuenta, por favor, todo estuvo delicioso.",
                    "¿Dónde está mi pasaporte?",
                    "Yo estudio español todos los días.",
                ],
            },
        ],
    },
    "fr": {
        "vocab": [
            {"id": "fr_cafe", "word": "le café", "translation": "the coffee", "pos": "noun (m)", "gender": "masculine", "roman": "luh ka-FAY", "icon": "coffee", "unit": 1, "note": "Masculine singular noun with 'le'."},
            {"id": "fr_croissant", "word": "un croissant chaud", "translation": "a warm croissant", "pos": "noun (m)", "gender": "masculine", "roman": "uhn krwa-SAHN shoh", "icon": "bread", "unit": 1, "note": "Final 't' and 'd' are silent in French."},
            {"id": "fr_eau", "word": "l'eau", "translation": "the water", "pos": "noun (f)", "gender": "feminine", "roman": "loh", "icon": "water", "unit": 1, "note": "'La' contracts to 'l'' before a vowel sound."},
            {"id": "fr_fromage", "word": "le fromage", "translation": "the cheese", "pos": "noun (m)", "gender": "masculine", "roman": "luh fro-MAZH", "icon": "cheese", "unit": 1, "note": "Masculine noun."},
            {"id": "fr_bonjour", "word": "bonjour, ça va ?", "translation": "hello, how are you?", "pos": "phrase", "gender": "n/a", "roman": "bohn-ZHOOR sa va", "icon": "sun", "unit": 1, "note": "Universal polite French greeting."},
            {"id": "fr_addition", "word": "l'addition, s'il vous plaît", "translation": "the bill, please", "pos": "phrase", "gender": "feminine", "roman": "la-dee-SYOHN seel voo PLEH", "icon": "receipt", "unit": 1, "note": "Polite way to ask for the check in a café."},
            {"id": "fr_gare", "word": "la gare du Nord", "translation": "the North train station", "pos": "noun (f)", "gender": "feminine", "roman": "la gar doo nor", "icon": "train", "unit": 2, "note": "'du' is the mandatory contraction of 'de + le'."},
            {"id": "fr_billet", "word": "un billet pour Paris", "translation": "a ticket to Paris", "pos": "phrase", "gender": "masculine", "roman": "uhn bee-YEH poor pa-REE", "icon": "ticket", "unit": 2, "note": "'ll' after 'i' makes a 'y' glide sound."},
            {"id": "fr_hotel", "word": "l'hôtel est près d'ici", "translation": "the hotel is near here", "pos": "sentence", "gender": "masculine", "roman": "loh-TEL eh preh dee-SEE", "icon": "hotel", "unit": 2, "note": "Silent 'h' triggers elision (l'hôtel)."},
            {"id": "fr_pomme", "word": "la pomme rouge", "translation": "the red apple", "pos": "noun (f)", "gender": "feminine", "roman": "la pom roozh", "icon": "apple", "unit": 3, "note": "Color adjectives come after the noun in French."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Je voudrais un café et un croissant, s'il vous plaît.",
                "english": "I would like a coffee and a croissant, please.",
                "tokens": ["Je", "voudrais", "un", "café", "et", "un", "croissant,", "s'il", "vous", "plaît."],
                "distractors": ["suis", "une", "eau", "sommes"],
                "gloss": {"Je": "I", "voudrais": "would like (conditional of vouloir)", "un": "a (masc)", "café": "coffee", "et": "and", "croissant,": "croissant", "s'il": "if it", "vous": "to you", "plaît.": "pleases"},
                "cloze_sentence": "Je ___ un café et un croissant, s'il vous plaît.",
                "cloze_answer": "voudrais",
                "cloze_options": ["voudrais", "voulez", "voulons", "suis"],
                "grammar_tip": "Use the conditional 'Je voudrais' (I would like) instead of 'Je veux' (I want) when ordering politely in France.",
                "dialogue_prompt": "Bonjour ! Qu'est-ce que je vous sers ce matin ?",
                "dialogue_prompt_en": "Hello! What can I get for you this morning?",
                "dialogue_options": [
                    "Je voudrais un café et un croissant, s'il vous plaît.",
                    "Le train part à huit heures.",
                    "J'habite près de la rivière.",
                ],
            },
            {
                "unit": 2,
                "target": "Excusez-moi, où est la gare, s'il vous plaît ?",
                "english": "Excuse me, where is the train station, please?",
                "tokens": ["Excusez-moi,", "où", "est", "la", "gare,", "s'il", "vous", "plaît", "?"],
                "distractors": ["ou", "sont", "le", "billet"],
                "gloss": {"Excusez-moi,": "Excuse me", "où": "where (with grave accent)", "est": "is (être)", "la": "the (fem)", "gare,": "train station", "s'il": "if it", "vous": "you", "plaît": "pleases", "?": "?"},
                "cloze_sentence": "Excusez-moi, ___ est la gare, s'il vous plaît ?",
                "cloze_answer": "où",
                "cloze_options": ["où", "ou", "qui", "que"],
                "grammar_tip": "'Où' with an accent grave means 'where'; 'ou' without an accent means 'or'.",
                "dialogue_prompt": "Nous devons prendre le TGV pour Lyon.",
                "dialogue_prompt_en": "We need to take the high-speed train to Lyon.",
                "dialogue_options": [
                    "Excusez-moi, où est la gare, s'il vous plaît ?",
                    "Le fromage est très bon.",
                    "Merci beaucoup, bonne soirée !",
                ],
            },
            {
                "unit": 3,
                "target": "L'addition, s'il vous plaît, c'était délicieux.",
                "english": "The bill, please, it was delicious.",
                "tokens": ["L'addition,", "s'il", "vous", "plaît,", "c'était", "délicieux."],
                "distractors": ["le", "table", "suis", "demain"],
                "gloss": {"L'addition,": "The bill", "s'il": "if it", "vous": "to you", "plaît,": "pleases", "c'était": "it was (imparfait)", "délicieux.": "delicious"},
                "cloze_sentence": "___, s'il vous plaît, c'était délicieux.",
                "cloze_answer": "L'addition",
                "cloze_options": ["L'addition", "La gare", "La voiture", "L'école"],
                "grammar_tip": "'C'était' (it was) uses the imparfait to describe how a meal or experience felt.",
                "dialogue_prompt": "Avez-vous terminé votre repas ?",
                "dialogue_prompt_en": "Have you finished your meal?",
                "dialogue_options": [
                    "L'addition, s'il vous plaît, c'était délicieux.",
                    "Je cherche mon passeport.",
                    "Bonjour, comment allez-vous ?",
                ],
            },
        ],
    },
    "ja": {
        "vocab": [
            {"id": "ja_kohi", "word": "コーヒー", "translation": "coffee", "pos": "noun", "gender": "n/a", "roman": "kōhī", "icon": "coffee", "unit": 1, "note": "Written in Katakana because it is a loanword."},
            {"id": "ja_mizu", "word": "みず (水)", "translation": "water", "pos": "noun", "gender": "n/a", "roman": "mizu", "icon": "water", "unit": 1, "note": "Often prefixed with polite 'o-' as おみず (omizu)."},
            {"id": "ja_ocha", "word": "おちゃ (お茶)", "translation": "green tea", "pos": "noun", "gender": "n/a", "roman": "ocha", "icon": "milk", "unit": 1, "note": "Honorific prefix お (o) + 茶 (cha)."},
            {"id": "ja_pan", "word": "パン", "translation": "bread", "pos": "noun", "gender": "n/a", "roman": "pan", "icon": "bread", "unit": 1, "note": "Borrowed from Portuguese 'pão' in the 16th century."},
            {"id": "ja_konnichiwa", "word": "こんにちは", "translation": "hello / good afternoon", "pos": "phrase", "gender": "n/a", "roman": "konnichiwa", "icon": "sun", "unit": 1, "note": "Final particle is written は (ha) but pronounced 'wa'."},
            {"id": "ja_eki", "word": "えき (駅)", "translation": "train station", "pos": "noun", "gender": "n/a", "roman": "eki", "icon": "train", "unit": 2, "note": "Used with Tokyo Station (東京駅 - Tōkyō-eki)."},
            {"id": "ja_kippu", "word": "きっぷ (切符)", "translation": "ticket", "pos": "noun", "gender": "n/a", "roman": "kippu", "icon": "ticket", "unit": 2, "note": "Small っ (tsu) doubles the following 'p' consonant."},
            {"id": "ja_okaikei", "word": "おかいけいをお願いします", "translation": "the check, please", "pos": "phrase", "gender": "n/a", "roman": "okaikei o onegaishimasu", "icon": "receipt", "unit": 3, "note": "Standard polite expression at restaurants in Japan."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "みずとコーヒーをください。",
                "english": "Water and coffee, please.",
                "tokens": ["みず", "と", "コーヒー", "を", "ください。"],
                "distractors": ["は", "どこ", "えき", "です"],
                "gloss": {"みず": "water (mizu)", "と": "and (connects nouns)", "コーヒー": "coffee (kōhī)", "を": "object marker (o)", "ください。": "please give me (kudasai)"},
                "cloze_sentence": "みずとコーヒー ___ ください。",
                "cloze_answer": "を",
                "cloze_options": ["を", "は", "が", "に"],
                "grammar_tip": "Use the direct object particle を (pronounced 'o') before ください (kudasai - please give me).",
                "dialogue_prompt": "いらっしゃいませ！ご注文はお決まりですか？",
                "dialogue_prompt_en": "Welcome! Have you decided on your order?",
                "dialogue_options": [
                    "みずとコーヒーをください。",
                    "えきはどこですか。",
                    "はじめまして、どうぞよろしく。",
                ],
            },
            {
                "unit": 2,
                "target": "すみません、えきはどこですか。",
                "english": "Excuse me, where is the train station?",
                "tokens": ["すみません、", "えき", "は", "どこ", "ですか。"],
                "distractors": ["を", "ください", "なに", "パン"],
                "gloss": {"すみません、": "Excuse me (sumimasen)", "えき": "train station (eki)", "は": "topic marker (wa)", "どこ": "where (doko)", "ですか。": "is it? (desu ka)"},
                "cloze_sentence": "すみません、えきは ___ ですか。",
                "cloze_answer": "どこ",
                "cloze_options": ["どこ", "なに", "だれ", "いつ"],
                "grammar_tip": "どこ (doko) means 'where'. Adding か (ka) at the end of です (desu) turns a statement into a polite question.",
                "dialogue_prompt": "新幹線（しんかんせん）に乗りたいです。",
                "dialogue_prompt_en": "I want to ride the Shinkansen bullet train.",
                "dialogue_options": [
                    "すみません、えきはどこですか。",
                    "おちゃはとてもおいしいです。",
                    "ごちそうさまでした。",
                ],
            },
        ],
    },
    "de": {
        "vocab": [
            {"id": "de_kaffee", "word": "der Kaffee", "translation": "the coffee", "pos": "noun (m)", "gender": "masculine (der)", "roman": "dehr KA-feh", "icon": "coffee", "unit": 1, "note": "All German nouns are capitalized; Kaffee is masculine (der)."},
            {"id": "de_wasser", "word": "das Wasser", "translation": "the water", "pos": "noun (n)", "gender": "neuter (das)", "roman": "das VA-ser", "icon": "water", "unit": 1, "note": "Neuter noun taking 'das'."},
            {"id": "de_brot", "word": "das Brot", "translation": "the bread", "pos": "noun (n)", "gender": "neuter (das)", "roman": "das broht", "icon": "bread", "unit": 1, "note": "Neuter noun."},
            {"id": "de_milch", "word": "die Milch", "translation": "the milk", "pos": "noun (f)", "gender": "feminine (die)", "roman": "dee milkh", "icon": "milk", "unit": 1, "note": "Feminine noun taking 'die'."},
            {"id": "de_bahnhof", "word": "der Bahnhof", "translation": "the train station", "pos": "noun (m)", "gender": "masculine (der)", "roman": "dehr BAHN-hohf", "icon": "train", "unit": 2, "note": "Compound of Bahn (rail) + Hof (court/station)."},
            {"id": "de_fahrkarte", "word": "die Fahrkarte", "translation": "the ticket", "pos": "noun (f)", "gender": "feminine (die)", "roman": "dee FAR-kar-tuh", "icon": "ticket", "unit": 2, "note": "Nouns ending in -e are usually feminine."},
            {"id": "de_rechnung", "word": "die Rechnung, bitte", "translation": "the bill, please", "pos": "phrase", "gender": "feminine (die)", "roman": "dee REKH-noong BI-tuh", "icon": "receipt", "unit": 3, "note": "Nouns ending in -ung are always feminine (die)."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Ich möchte einen Kaffee und ein Brot, bitte.",
                "english": "I would like a coffee and a bread, please.",
                "tokens": ["Ich", "möchte", "einen", "Kaffee", "und", "ein", "Brot,", "bitte."],
                "distractors": ["einem", "bist", "Wasser", "die"],
                "gloss": {"Ich": "I", "möchte": "would like", "einen": "a (masc accusative)", "Kaffee": "coffee", "und": "and", "ein": "a (neuter)", "Brot,": "bread", "bitte.": "please"},
                "cloze_sentence": "Ich möchte ___ Kaffee und ein Brot, bitte.",
                "cloze_answer": "einen",
                "cloze_options": ["einen", "ein", "eine", "einer"],
                "grammar_tip": "Because 'der Kaffee' is masculine and is the direct object (Accusative case), 'ein' changes to 'einen'!",
                "dialogue_prompt": "Guten Morgen! Was möchten Sie bestellen?",
                "dialogue_prompt_en": "Good morning! What would you like to order?",
                "dialogue_options": [
                    "Ich möchte einen Kaffee und ein Brot, bitte.",
                    "Der Bahnhof ist geradeaus.",
                    "Auf Wiedersehen und danke!",
                ],
            },
            {
                "unit": 2,
                "target": "Entschuldigung, wo ist der Bahnhof?",
                "english": "Excuse me, where is the train station?",
                "tokens": ["Entschuldigung,", "wo", "ist", "der", "Bahnhof?"],
                "distractors": ["sind", "die", "Kaffee", "wer"],
                "gloss": {"Entschuldigung,": "Excuse me", "wo": "where", "ist": "is", "der": "the (masc nominative)", "Bahnhof?": "train station"},
                "cloze_sentence": "Entschuldigung, ___ ist der Bahnhof?",
                "cloze_answer": "wo",
                "cloze_options": ["wo", "wer", "was", "wann"],
                "grammar_tip": "'Wo' means 'where' (static location), while 'wohin' means 'where to' (motion).",
                "dialogue_prompt": "Wir suchen den Zug nach Berlin.",
                "dialogue_prompt_en": "We are looking for the train to Berlin.",
                "dialogue_options": [
                    "Entschuldigung, wo ist der Bahnhof?",
                    "Das Wasser ist sehr kalt.",
                    "Die Rechnung, bitte!",
                ],
            },
        ],
    },
    "it": {
        "vocab": [
            {"id": "it_caffe", "word": "il caffè", "translation": "the coffee", "pos": "noun (m)", "gender": "masculine", "roman": "eel kaf-FEH", "icon": "coffee", "unit": 1, "note": "Grave accent on final è marks stressed open vowel."},
            {"id": "it_acqua", "word": "l'acqua", "translation": "the water", "pos": "noun (f)", "gender": "feminine", "roman": "LAK-kwa", "icon": "water", "unit": 1, "note": "Spelled with -cqu- and takes l' before vowel."},
            {"id": "it_cornetto", "word": "un cornetto", "translation": "a croissant", "pos": "noun (m)", "gender": "masculine", "roman": "oon kor-NET-to", "icon": "bread", "unit": 1, "note": "Pronounce the double 'tt' distinctly."},
            {"id": "it_stazione", "word": "la stazione", "translation": "the train station", "pos": "noun (f)", "gender": "feminine", "roman": "la stat-SYO-neh", "icon": "train", "unit": 2, "note": "Feminine singular."},
            {"id": "it_conto", "word": "il conto, per favore", "translation": "the bill, please", "pos": "phrase", "gender": "masculine", "roman": "eel KON-to per fa-VO-reh", "icon": "receipt", "unit": 3, "note": "Polite restaurant phrase."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Vorrei un caffè e un cornetto, per favore.",
                "english": "I would like a coffee and a croissant, please.",
                "tokens": ["Vorrei", "un", "caffè", "e", "un", "cornetto,", "per", "favore."],
                "distractors": ["sono", "l'acqua", "la", "stazione"],
                "gloss": {"Vorrei": "I would like", "un": "a", "caffè": "coffee", "e": "and", "cornetto,": "croissant", "per": "for", "favore.": "favor (please)"},
                "cloze_sentence": "___ un caffè e un cornetto, per favore.",
                "cloze_answer": "Vorrei",
                "cloze_options": ["Vorrei", "Voglio", "Siamo", "Avete"],
                "grammar_tip": "'Vorrei' is the conditional of 'volere' (to want) — the polite way to order in Italy.",
                "dialogue_prompt": "Buongiorno! Cosa prende oggi?",
                "dialogue_prompt_en": "Good morning! What are you having today?",
                "dialogue_options": [
                    "Vorrei un caffè e un cornetto, per favore.",
                    "Dov'è la stazione dei treni?",
                    "Arrivederci e grazie!",
                ],
            }
        ],
    },
    "ko": {
        "vocab": [
            {"id": "ko_keopi", "word": "커피", "translation": "coffee", "pos": "noun", "gender": "n/a", "roman": "keo-pi", "icon": "coffee", "unit": 1, "note": "Loanword written in Hangul blocks."},
            {"id": "ko_mul", "word": "물", "translation": "water", "pos": "noun", "gender": "n/a", "roman": "mul", "icon": "water", "unit": 1, "note": "Single syllable block: ㅁ(m) + ㅜ(u) + ㄹ(l)."},
            {"id": "ko_ppang", "word": "빵", "translation": "bread", "pos": "noun", "gender": "n/a", "roman": "ppang", "icon": "bread", "unit": 1, "note": "Uses tense double consonant ㅃ (pp)."},
            {"id": "ko_yeok", "word": "기차역", "translation": "train station", "pos": "noun", "gender": "n/a", "roman": "gi-cha-yeok", "icon": "train", "unit": 2, "note": "기차 (train) + 역 (station)."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "커피하고 물 주세요.",
                "english": "Please give me coffee and water.",
                "tokens": ["커피", "하고", "물", "주세요."],
                "distractors": ["어디", "기차역", "은", "가요"],
                "gloss": {"커피": "coffee", "하고": "and / with", "물": "water", "주세요.": "please give me (juseyo)"},
                "cloze_sentence": "커피하고 물 ___.",
                "cloze_answer": "주세요",
                "cloze_options": ["주세요", "입니다", "없어요", "갑니다"],
                "grammar_tip": "Noun + 주세요 (juseyo) is the universal polite pattern for requesting items in Korean.",
                "dialogue_prompt": "어서 오세요! 무엇을 드릴까요?",
                "dialogue_prompt_en": "Welcome! What can I get for you?",
                "dialogue_options": [
                    "커피하고 물 주세요.",
                    "기차역이 어디에 있어요?",
                    "안녕히 계세요.",
                ],
            }
        ],
    },
    "zh": {
        "vocab": [
            {"id": "zh_kafei", "word": "咖啡 (kāfēi)", "translation": "coffee", "pos": "noun", "gender": "n/a", "roman": "kāfēi", "icon": "coffee", "unit": 1, "note": "Both syllables use the high-level 1st tone."},
            {"id": "zh_shui", "word": "水 (shuǐ)", "translation": "water", "pos": "noun", "gender": "n/a", "roman": "shuǐ", "icon": "water", "unit": 1, "note": "Dipping 3rd tone."},
            {"id": "zh_cha", "word": "茶 (chá)", "translation": "tea", "pos": "noun", "gender": "n/a", "roman": "chá", "icon": "milk", "unit": 1, "note": "Rising 2nd tone."},
            {"id": "zh_huochezhan", "word": "火车站 (huǒchēzhàn)", "translation": "train station", "pos": "noun", "gender": "n/a", "roman": "huǒchēzhàn", "icon": "train", "unit": 2, "note": "Literally 'fire-vehicle-station'."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "我要一杯咖啡，谢谢。",
                "english": "I want a cup of coffee, thank you.",
                "tokens": ["我", "要", "一杯", "咖啡，", "谢谢。"],
                "distractors": ["不", "火车站", "哪里", "是"],
                "gloss": {"我": "I (wǒ)", "要": "want (yào)", "一杯": "one cup of (yì bēi)", "咖啡，": "coffee (kāfēi)", "谢谢。": "thank you (xièxie)"},
                "cloze_sentence": "我 ___ 一杯咖啡，谢谢。",
                "cloze_answer": "要",
                "cloze_options": ["要", "是", "在", "吗"],
                "grammar_tip": "Measure words like 杯 (bēi - cup) are required between a number and a noun in Mandarin.",
                "dialogue_prompt": "您好！请问您想喝点什么？",
                "dialogue_prompt_en": "Hello! May I ask what you would like to drink?",
                "dialogue_options": [
                    "我要一杯咖啡，谢谢。",
                    "请问火车站在哪里？",
                    "再见，明天见！",
                ],
            }
        ],
    },
    "pt": {
        "vocab": [
            {"id": "pt_cafe", "word": "o café", "translation": "the coffee", "pos": "noun (m)", "gender": "masculine", "roman": "oo ka-FEH", "icon": "coffee", "unit": 1, "note": "Masculine singular uses 'o' in Portuguese."},
            {"id": "pt_agua", "word": "a água", "translation": "the water", "pos": "noun (f)", "gender": "feminine", "roman": "a AH-gwa", "icon": "water", "unit": 1, "note": "Feminine singular uses 'a'."},
            {"id": "pt_pao", "word": "o pão de queijo", "translation": "the cheese bread", "pos": "noun (m)", "gender": "masculine", "roman": "oo pown jee KAY-zhoo", "icon": "bread", "unit": 1, "note": "Iconic Brazilian baked snack; ã marks nasal vowel."},
            {"id": "pt_estacao", "word": "a estação de trem", "translation": "the train station", "pos": "noun (f)", "gender": "feminine", "roman": "a es-ta-SOWN jee treyn", "icon": "train", "unit": 2, "note": "-ção corresponds to English '-tion'."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Eu quero um café e um pão de queijo, por favor.",
                "english": "I want a coffee and a cheese bread, please.",
                "tokens": ["Eu", "quero", "um", "café", "e", "um", "pão", "de", "queijo,", "por", "favor."],
                "distractors": ["uma", "água", "onde", "estação"],
                "gloss": {"Eu": "I", "quero": "want", "um": "a (masc)", "café": "coffee", "e": "and", "pão": "bread", "de": "of", "queijo,": "cheese", "por": "by/for", "favor.": "favor (please)"},
                "cloze_sentence": "Eu ___ um café e um pão de queijo, por favor.",
                "cloze_answer": "quero",
                "cloze_options": ["quero", "queremos", "sou", "estou"],
                "grammar_tip": "'Eu quero' is first-person singular of 'querer' (to want).",
                "dialogue_prompt": "Bom dia! O que você gostaria de pedir?",
                "dialogue_prompt_en": "Good morning! What would you like to order?",
                "dialogue_options": [
                    "Eu quero um café e um pão de queijo, por favor.",
                    "Onde fica a estação de trem?",
                    "Muito obrigado e até logo!",
                ],
            }
        ],
    },
    "ru": {
        "vocab": [
            {"id": "ru_kofe", "word": "кофе", "translation": "coffee", "pos": "noun", "gender": "masculine", "roman": "KO-fye", "icon": "coffee", "unit": 1, "note": "Russian has no articles ('a' or 'the')."},
            {"id": "ru_voda", "word": "вода", "translation": "water", "pos": "noun", "gender": "feminine", "roman": "va-DA", "icon": "water", "unit": 1, "note": "Unstressed 'o' is pronounced like 'a' (akanye)."},
            {"id": "ru_khleb", "word": "хлеб", "translation": "bread", "pos": "noun", "gender": "masculine", "roman": "khlyep", "icon": "bread", "unit": 1, "note": "Starts with Cyrillic Х (kh sound)."},
            {"id": "ru_vokzal", "word": "вокзал", "translation": "train station", "pos": "noun", "gender": "masculine", "roman": "vak-ZAL", "icon": "train", "unit": 2, "note": "Major railway terminal."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "Можно кофе и воду, пожалуйста?",
                "english": "May I have coffee and water, please?",
                "tokens": ["Можно", "кофе", "и", "воду,", "пожалуйста?"],
                "distractors": ["где", "вокзал", "нет", "мой"],
                "gloss": {"Можно": "May I have / Is it possible", "кофе": "coffee", "и": "and", "воду,": "water (accusative of вода)", "пожалуйста?": "please"},
                "cloze_sentence": "Можно кофе и ___, пожалуйста?",
                "cloze_answer": "воду",
                "cloze_options": ["воду", "вода", "воды", "воде"],
                "grammar_tip": "Feminine nouns ending in -а change to -у in the Accusative case (вода → воду).",
                "dialogue_prompt": "Здравствуйте! Что вы будете заказывать?",
                "dialogue_prompt_en": "Hello! What will you be ordering?",
                "dialogue_options": [
                    "Можно кофе и воду, пожалуйста?",
                    "Скажите, где находится вокзал?",
                    "Большое спасибо, до свидания!",
                ],
            }
        ],
    },
    "ar": {
        "vocab": [
            {"id": "ar_qahwa", "word": "قهوة (qahwa)", "translation": "coffee", "pos": "noun (f)", "gender": "feminine", "roman": "QAH-wa", "icon": "coffee", "unit": 1, "note": "Ends with tāʾ marbūṭa (ة), marking feminine gender."},
            {"id": "ar_maa", "word": "ماء (māʾ)", "translation": "water", "pos": "noun (m)", "gender": "masculine", "roman": "maa'", "icon": "water", "unit": 1, "note": "Ends with hamza (ء) glottal stop."},
            {"id": "ar_khubz", "word": "خبز (khubz)", "translation": "bread", "pos": "noun (m)", "gender": "masculine", "roman": "khubz", "icon": "bread", "unit": 1, "note": "Root kh-b-z relates to baking."},
            {"id": "ar_mahatta", "word": "محطة القطار (maḥaṭṭat al-qiṭār)", "translation": "the train station", "pos": "noun (f)", "gender": "feminine", "roman": "ma-HAT-tat al-qi-TAR", "icon": "train", "unit": 2, "note": "Idafa (possessive construct): station of the train."},
        ],
        "sentences": [
            {
                "unit": 1,
                "target": "أريد قهوة وماء من فضلك.",
                "english": "I want coffee and water, please.",
                "tokens": ["أريد", "قهوة", "وماء", "من", "فضلك."],
                "distractors": ["أين", "محطة", "لا", "هذا"],
                "gloss": {"أريد": "I want (urīdu)", "قهوة": "coffee (qahwa)", "وماء": "and water (wa-māʾ)", "من": "from (min)", "فضلك.": "your kindness / please (faḍlik)"},
                "cloze_sentence": "___ قهوة وماء من فضلك.",
                "cloze_answer": "أريد",
                "cloze_options": ["أريد", "أين", "كيف", "نحن"],
                "grammar_tip": "أريد (urīdu) means 'I want'; prefix أ- (u-) marks first-person singular present tense.",
                "dialogue_prompt": "مرحباً! ماذا تحب أن تشرب اليوم؟",
                "dialogue_prompt_en": "Welcome! What would you like to drink today?",
                "dialogue_options": [
                    "أريد قهوة وماء من فضلك.",
                    "أين محطة القطار؟",
                    "شكراً جزيلاً ومع السلامة.",
                ],
            }
        ],
    },
}


def build_course_units(lang_code: str) -> List[Dict[str, Any]]:
    """Builds the structured CEFR skill-tree units & stepping-stone nodes for a language."""
    lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
    pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
    vocab = pack["vocab"]
    sentences = pack["sentences"]

    v0 = vocab[0] if len(vocab) > 0 else LANGUAGE_PACKS["es"]["vocab"][0]
    v1 = vocab[1] if len(vocab) > 1 else LANGUAGE_PACKS["es"]["vocab"][1]
    v2 = vocab[2] if len(vocab) > 2 else LANGUAGE_PACKS["es"]["vocab"][2]
    v3 = vocab[3] if len(vocab) > 3 else LANGUAGE_PACKS["es"]["vocab"][0]
    s0 = sentences[0]
    s1 = sentences[1] if len(sentences) > 1 else sentences[0]
    s2 = sentences[2] if len(sentences) > 2 else sentences[0]

    return [
        {
            "unit_number": 1,
            "id": f"{lang_code}_unit_1",
            "section": "Section 1: CEFR A1 Rookie",
            "title": "Unit 1: Order in a Café & Polite Greetings",
            "subtitle": f"Introduce yourself, order drinks & pastries, and use polite {lang['name']} requests.",
            "color": "#58cc02",
            "border_color": "#46a302",
            "guidebook": {
                "title": f"Unit 1 Guidebook: Café & Greetings ({lang['name']})",
                "summary": f"Master foundational {lang['name']} nouns, gender/articles, and polite ordering verbs.",
                "grammar_tip": s0["grammar_tip"],
                "cultural_note": f"In {lang['name']}-speaking cafés, always greet the staff before placing your order.",
                "key_phrases": [
                    {"native": s0["target"], "english": s0["english"]},
                    {"native": v0["word"], "english": v0["translation"]},
                    {"native": v1["word"], "english": v1["translation"]},
                    {"native": v2["word"], "english": v2["translation"]},
                ],
            },
            "nodes": [
                {
                    "id": f"{lang_code}_u1_n1",
                    "type": "lesson",
                    "title": "Café Essentials",
                    "subtitle": "Coffee, Water & Polite Orders",
                    "icon": "star",
                    "offset_x": 0,
                    "max_crowns": 5,
                    "xp_reward": 20,
                },
                {
                    "id": f"{lang_code}_u1_n2",
                    "type": "lesson",
                    "title": "Bakery & Prices",
                    "subtitle": "Sentence Building & Listening",
                    "icon": "book",
                    "offset_x": -58,
                    "max_crowns": 5,
                    "xp_reward": 25,
                },
                {
                    "id": f"{lang_code}_u1_story",
                    "type": "story",
                    "story_id": f"{lang_code}_story_cafe",
                    "title": "Story: Morning at the Café",
                    "subtitle": "Interactive Voiced Story (+30 XP)",
                    "icon": "story",
                    "offset_x": -82,
                    "max_crowns": 1,
                    "xp_reward": 30,
                },
                {
                    "id": f"{lang_code}_u1_roleplay",
                    "type": "roleplay",
                    "scenario_id": f"{lang_code}_rp_cafe",
                    "title": "MAX Roleplay: The Artisanal Barista",
                    "subtitle": "Duolingo Max Live AI Conversation",
                    "icon": "max",
                    "offset_x": -40,
                    "max_crowns": 1,
                    "xp_reward": 40,
                },
                {
                    "id": f"{lang_code}_u1_practice",
                    "type": "practice",
                    "title": "Personalized SRS Practice",
                    "subtitle": "Strengthen Weak Words & Refill Heart",
                    "icon": "dumbbell",
                    "offset_x": 38,
                    "max_crowns": 3,
                    "xp_reward": 20,
                },
                {
                    "id": f"{lang_code}_u1_trophy",
                    "type": "trophy",
                    "title": "Unit 1 Legendary Review",
                    "subtitle": "Complete all 8 exercise mechanics",
                    "icon": "trophy",
                    "offset_x": 0,
                    "max_crowns": 1,
                    "xp_reward": 50,
                },
            ],
        },
        {
            "unit_number": 2,
            "id": f"{lang_code}_unit_2",
            "section": "Section 1: CEFR A1 Explorer",
            "title": "Unit 2: Navigate Trains, Hotels & Directions",
            "subtitle": f"Ask where stations are, buy rail tickets, and check into hotels in {lang['name']}.",
            "color": "#1cb0f6",
            "border_color": "#1899d6",
            "guidebook": {
                "title": f"Unit 2 Guidebook: Transit & Directions ({lang['name']})",
                "summary": "Ask for locations politely, purchase transit tickets, and handle travel checkpoints.",
                "grammar_tip": s1["grammar_tip"],
                "cultural_note": "High-speed rail is central to intercity travel; ticket counters appreciate polite openings.",
                "key_phrases": [
                    {"native": s1["target"], "english": s1["english"]},
                    {"native": v3["word"], "english": v3["translation"]},
                ],
            },
            "nodes": [
                {
                    "id": f"{lang_code}_u2_n1",
                    "type": "lesson",
                    "title": "Stations & Tickets",
                    "subtitle": "Asking Directions & Transit",
                    "icon": "star",
                    "offset_x": 52,
                    "max_crowns": 5,
                    "xp_reward": 25,
                },
                {
                    "id": f"{lang_code}_u2_roleplay",
                    "type": "roleplay",
                    "scenario_id": f"{lang_code}_rp_station",
                    "title": "MAX Roleplay: Express Train Counter",
                    "subtitle": "Duolingo Max Live AI Conversation",
                    "icon": "max",
                    "offset_x": 76,
                    "max_crowns": 1,
                    "xp_reward": 40,
                },
                {
                    "id": f"{lang_code}_u2_story",
                    "type": "story",
                    "story_id": f"{lang_code}_story_passport",
                    "title": "Story: The Missing Passport",
                    "subtitle": "Interactive Voiced Mystery (+35 XP)",
                    "icon": "story",
                    "offset_x": 32,
                    "max_crowns": 1,
                    "xp_reward": 35,
                },
                {
                    "id": f"{lang_code}_u2_trophy",
                    "type": "trophy",
                    "title": "Unit 2 Legendary Trophy",
                    "subtitle": "Master Transit & Directions",
                    "icon": "trophy",
                    "offset_x": 0,
                    "max_crowns": 1,
                    "xp_reward": 50,
                },
            ],
        },
        {
            "unit_number": 3,
            "id": f"{lang_code}_unit_3",
            "section": "Section 2: CEFR A2 Traveler",
            "title": "Unit 3: Dining Out, Markets & Compliments",
            "subtitle": "Request the check, compliment the chef, and shop for fresh ingredients.",
            "color": "#ce82ff",
            "border_color": "#a55eea",
            "guidebook": {
                "title": f"Unit 3 Guidebook: Dining & Market ({lang['name']})",
                "summary": "Express past satisfaction, ask for the bill, and pair adjectives with nouns.",
                "grammar_tip": s2["grammar_tip"],
                "cultural_note": "In most European and Latin American restaurants, the server only brings the bill when you ask for it.",
                "key_phrases": [
                    {"native": s2["target"], "english": s2["english"]},
                ],
            },
            "nodes": [
                {
                    "id": f"{lang_code}_u3_n1",
                    "type": "lesson",
                    "title": "Restaurant & Check",
                    "subtitle": "Ordering & Paying Politely",
                    "icon": "star",
                    "offset_x": -48,
                    "max_crowns": 5,
                    "xp_reward": 30,
                },
                {
                    "id": f"{lang_code}_u3_trophy",
                    "type": "trophy",
                    "title": "Unit 3 Legendary Trophy",
                    "subtitle": "CEFR A2 Milestone Challenge",
                    "icon": "trophy",
                    "offset_x": 0,
                    "max_crowns": 1,
                    "xp_reward": 60,
                },
            ],
        },
    ]


def build_lesson_exercises(lang_code: str, node_id: str) -> List[Dict[str, Any]]:
    """
    Generates a full 8-exercise interactive Duolingo lesson covering all 8 signature mechanics:
    1. visual_select (2x2 SVG Illustrated Flashcards)
    2. word_bank (Tap-tile sentence builder with hover dictionary tooltips)
    3. listening (Tap what you hear with 1.0x + 0.65x Slow Turtle button)
    4. cloze (Fill-in-the-blank grammar & conjugation challenge)
    5. dialogue (Two-character mini-conversation response)
    6. speaking (Voice pronunciation grader + waveform)
    7. match_pairs (5x2 Match Madness vocabulary pair grid)
    8. free_type (Keyboard translation with Levenshtein typo tolerance & accent bar)
    """
    pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
    vocab = pack["vocab"]
    sentences = pack["sentences"]

    # Pick unit index based on node_id
    unit_idx = 0
    if "_u2_" in node_id and len(sentences) > 1:
        unit_idx = 1
    elif "_u3_" in node_id and len(sentences) > 2:
        unit_idx = 2

    s_primary = sentences[unit_idx % len(sentences)]
    s_secondary = sentences[(unit_idx + 1) % len(sentences)]

    # Ensure at least 4 vocab items for visual cards & match pairs
    v_items = list(vocab)
    while len(v_items) < 5:
        v_items.append(vocab[len(v_items) % len(vocab)])

    target_v = v_items[unit_idx % len(v_items)]
    card_choices = [target_v]
    for cand in v_items:
        if cand["id"] != target_v["id"] and len(card_choices) < 4:
            card_choices.append(cand)

    exercises: List[Dict[str, Any]] = [
        # 1. Illustrated Visual Flashcard Selection
        {
            "id": f"{node_id}_ex1_visual",
            "type": "visual_select",
            "badge": "NEW WORD",
            "prompt": f"Select the correct image for “{target_v['translation']}”",
            "target_word_id": target_v["id"],
            "answer": target_v["word"],
            "audio_text": target_v["word"],
            "explanation": f"“{target_v['word']}” means “{target_v['translation']}”. {target_v['note']}",
            "cards": [
                {
                    "word": c["word"],
                    "translation": c["translation"],
                    "roman": c["roman"],
                    "icon": c["icon"],
                }
                for c in card_choices
            ],
        },
        # 2. Tap-Tile Word Bank Sentence Builder
        {
            "id": f"{node_id}_ex2_wordbank",
            "type": "word_bank",
            "badge": "SENTENCE BUILDER",
            "prompt": "Write this in English or Target Language — Tap the words in order:",
            "direction": "to_target",
            "source_text": s_primary["english"],
            "audio_text": s_primary["target"],
            "answer": s_primary["target"],
            "tokens": s_primary["tokens"],
            "distractors": s_primary["distractors"],
            "gloss": s_primary["gloss"],
            "explanation": s_primary["grammar_tip"],
            "target_word_id": target_v["id"],
        },
        # 3. Listening Lab (Normal 1.0x + Slow Turtle 0.65x)
        {
            "id": f"{node_id}_ex3_listening",
            "type": "listening",
            "badge": "LISTENING LAB",
            "prompt": "Tap what you hear",
            "audio_text": s_secondary["target"],
            "answer": s_secondary["target"],
            "english_translation": s_secondary["english"],
            "tokens": s_secondary["tokens"],
            "distractors": s_secondary["distractors"][:3],
            "explanation": f"Audio transcript: “{s_secondary['target']}” ({s_secondary['english']}). {s_secondary['grammar_tip']}",
            "target_word_id": v_items[1]["id"],
        },
        # 4. Cloze / Fill-in-the-Blank Grammar
        {
            "id": f"{node_id}_ex4_cloze",
            "type": "cloze",
            "badge": "GRAMMAR FOCUS",
            "prompt": "Complete the sentence with the correct grammatical form:",
            "sentence_template": s_primary["cloze_sentence"],
            "english_hint": s_primary["english"],
            "audio_text": s_primary["target"],
            "answer": s_primary["cloze_answer"],
            "options": s_primary["cloze_options"],
            "explanation": s_primary["grammar_tip"],
            "target_word_id": target_v["id"],
        },
        # 5. Mini-Dialogue / Conversation Completion
        {
            "id": f"{node_id}_ex5_dialogue",
            "type": "dialogue",
            "badge": "CONVERSATION",
            "prompt": "Choose the most natural response to complete the conversation:",
            "speaker_line": s_primary["dialogue_prompt"],
            "speaker_line_en": s_primary["dialogue_prompt_en"],
            "audio_text": s_primary["dialogue_prompt"],
            "answer": s_primary["dialogue_options"][0],
            "options": s_primary["dialogue_options"],
            "explanation": f"“{s_primary['dialogue_options'][0]}” directly answers “{s_primary['dialogue_prompt']}”.",
            "target_word_id": v_items[2]["id"],
        },
        # 6. Speaking & Pronunciation Grader
        {
            "id": f"{node_id}_ex6_speaking",
            "type": "speaking",
            "badge": "SPEAKING LAB",
            "prompt": "Speak this sentence out loud:",
            "target_sentence": s_primary["target"],
            "english_hint": s_primary["english"],
            "audio_text": s_primary["target"],
            "answer": s_primary["target"],
            "explanation": f"Pronunciation check for “{s_primary['target']}”. {s_primary['grammar_tip']}",
            "target_word_id": target_v["id"],
        },
        # 7. Match Madness (Timed 5x2 Pair Grid)
        {
            "id": f"{node_id}_ex7_match",
            "type": "match_pairs",
            "badge": "MATCH MADNESS",
            "prompt": "Tap the matching pairs! Clear the board to build your combo:",
            "answer": "ALL_MATCHED",
            "pairs": [
                {"id": c["id"], "left": c["word"], "right": c["translation"]}
                for c in v_items[:5]
            ],
            "explanation": "Great job matching all 5 vocabulary pairs with zero errors!",
            "target_word_id": v_items[0]["id"],
        },
        # 8. Free-Type Translation with Levenshtein Typo Tolerance
        {
            "id": f"{node_id}_ex8_freetype",
            "type": "free_type",
            "badge": "HARD EXERCISE (+2x XP)",
            "prompt": f"Translate this sentence into {LANGUAGES.get(lang_code, LANGUAGES['es'])['name']}:",
            "source_text": s_primary["english"],
            "audio_text": s_primary["target"],
            "answer": s_primary["target"],
            "accepted_answers": [
                s_primary["target"],
                s_primary["target"].rstrip(".?!"),
            ],
            "explanation": s_primary["grammar_tip"],
            "target_word_id": target_v["id"],
        },
    ]
    return exercises


def build_stories(lang_code: str) -> List[Dict[str, Any]]:
    """Returns Interactive Voiced Duolingo Stories for the active language."""
    lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
    pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
    s0 = pack["sentences"][0]
    s1 = pack["sentences"][1] if len(pack["sentences"]) > 1 else s0

    if lang_code == "es":
        return [
            {
                "id": "es_story_cafe",
                "title": "Un Café en Madrid",
                "english_title": "A Coffee in Madrid",
                "set": "Set 1 • CEFR A1",
                "xp_reward": 30,
                "gems_reward": 15,
                "cover_icon": "coffee",
                "cover_color": "#ff9600",
                "lines": [
                    {"speaker": "Narrator", "avatar": "🦉", "text": "Lucía entra en una cafetería muy ocupada en Madrid.", "en": "Lucía walks into a very busy café in Madrid."},
                    {"speaker": "Camarero", "avatar": "👨‍🍳", "text": "¡Buenos días! ¿Qué desea tomar hoy?", "en": "Good morning! What would you like to drink today?"},
                    {
                        "speaker": "Lucía",
                        "avatar": "👩🏽",
                        "text": "Yo quiero un café con leche, por favor.",
                        "en": "I want a coffee with milk, please.",
                        "question": {
                            "prompt": "What is Lucía ordering?",
                            "options": ["A coffee with milk", "A glass of cold water", "A train ticket to Madrid"],
                            "answer": "A coffee with milk",
                        },
                    },
                    {"speaker": "Camarero", "avatar": "👨‍🍳", "text": "¿Con azúcar o con sal?", "en": "With sugar or with salt?"},
                    {"speaker": "Lucía", "avatar": "👩🏽", "text": "¡Con azúcar, claro! Pero este café tiene... ¡sal!", "en": "With sugar, of course! But this coffee has... salt!"},
                    {
                        "speaker": "Camarero",
                        "avatar": "👨‍🍳",
                        "text": "¡Ay, lo siento! Necesito otro café para mí también.",
                        "en": "Oh, I'm sorry! I need another coffee for myself too.",
                        "question": {
                            "prompt": "Why did the waiter accidentally put salt in Lucía's coffee?",
                            "options": ["He is sleepy and needs coffee himself", "Lucía asked for salt", "The café ran out of milk"],
                            "answer": "He is sleepy and needs coffee himself",
                        },
                    },
                ],
            },
            {
                "id": "es_story_passport",
                "title": "El Pasaporte Perdido",
                "english_title": "The Missing Passport",
                "set": "Set 1 • CEFR A1",
                "xp_reward": 35,
                "gems_reward": 20,
                "cover_icon": "passport",
                "cover_color": "#1cb0f6",
                "lines": [
                    {"speaker": "Narrator", "avatar": "🦉", "text": "Mateo y Sofía están en la estación de tren.", "en": "Mateo and Sofía are at the train station."},
                    {"speaker": "Mateo", "avatar": "🧔🏻", "text": "Sofía, nuestro tren sale en cinco minutos. ¿Dónde está mi pasaporte?", "en": "Sofía, our train leaves in five minutes. Where is my passport?"},
                    {
                        "speaker": "Sofía",
                        "avatar": "👩🏻",
                        "text": "¿No está en tu chaqueta?",
                        "en": "Isn't it in your jacket?",
                        "question": {
                            "prompt": "Where does Sofía think the passport is?",
                            "options": ["In Mateo's jacket", "At the hotel", "Inside a suitcase"],
                            "answer": "In Mateo's jacket",
                        },
                    },
                    {"speaker": "Mateo", "avatar": "🧔🏻", "text": "¡No! ¡Solo tengo un pan y queso en mi chaqueta!", "en": "No! I only have bread and cheese in my jacket!"},
                    {
                        "speaker": "Sofía",
                        "avatar": "👩🏻",
                        "text": "Mateo... mira tu mano izquierda. ¡Tienes el pasaporte en la mano!",
                        "en": "Mateo... look at your left hand. You are holding the passport in your hand!",
                        "question": {
                            "prompt": "Where was Mateo's passport the whole time?",
                            "options": ["In his left hand", "At the café", "On the train"],
                            "answer": "In his left hand",
                        },
                    },
                ],
            },
        ]

    # Dynamic localized stories for any other selected language
    return [
        {
            "id": f"{lang_code}_story_cafe",
            "title": f"Morning at the {lang['name']} Café",
            "english_title": f"Polite Ordering in {lang['native_name']}",
            "set": "Set 1 • CEFR A1",
            "xp_reward": 30,
            "gems_reward": 15,
            "cover_icon": "coffee",
            "cover_color": "#ff9600",
            "lines": [
                {"speaker": "Barista", "avatar": "👨‍🍳", "text": s0["dialogue_prompt"], "en": s0["dialogue_prompt_en"]},
                {
                    "speaker": "Traveler",
                    "avatar": "🧑🏽",
                    "text": s0["target"],
                    "en": s0["english"],
                    "question": {
                        "prompt": f"What does “{s0['target']}” mean?",
                        "options": [s0["english"], "Where is my hotel room?", "The train leaves tomorrow morning."],
                        "answer": s0["english"],
                    },
                },
                {
                    "speaker": "Barista",
                    "avatar": "👨‍🍳",
                    "text": pack["vocab"][0]["word"] + " — " + pack["vocab"][1]["word"] + "!",
                    "en": f"Coming right up: {pack['vocab'][0]['translation']} and {pack['vocab'][1]['translation']}!",
                    "question": {
                        "prompt": f"Which word means “{pack['vocab'][0]['translation']}”?",
                        "options": [pack["vocab"][0]["word"], pack["vocab"][1]["word"], pack["vocab"][-1]["word"]],
                        "answer": pack["vocab"][0]["word"],
                    },
                },
            ],
        },
        {
            "id": f"{lang_code}_story_passport",
            "title": "Express Train Adventure",
            "english_title": f"Finding the Station in {lang['native_name']}",
            "set": "Set 1 • CEFR A1",
            "xp_reward": 35,
            "gems_reward": 20,
            "cover_icon": "train",
            "cover_color": "#1cb0f6",
            "lines": [
                {"speaker": "Companion", "avatar": "👩🏻", "text": s1["dialogue_prompt"], "en": s1["dialogue_prompt_en"]},
                {
                    "speaker": "Traveler",
                    "avatar": "🧔🏻",
                    "text": s1["target"],
                    "en": s1["english"],
                    "question": {
                        "prompt": "What is the traveler asking or stating?",
                        "options": [s1["english"], "Everything was delicious.", "I only drink cold milk."],
                        "answer": s1["english"],
                    },
                },
            ],
        },
    ]


def build_roleplay_scenarios(lang_code: str) -> List[Dict[str, Any]]:
    """Returns Duolingo Max AI Roleplay Scenarios for the active language."""
    lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
    pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
    s0 = pack["sentences"][0]
    s1 = pack["sentences"][1] if len(pack["sentences"]) > 1 else s0

    return [
        {
            "id": f"{lang_code}_rp_cafe",
            "title": f"The Artisanal Café ({lang['native_name']})",
            "location": "Corner Espresso & Pastry Bar",
            "cefr": "CEFR A1",
            "xp_reward": 40,
            "npc_name": "Mateo (Barista)" if lang_code == "es" else f"Chef ({lang['name']} Barista)",
            "npc_avatar": "👨‍🍳",
            "objective": f"Greet the barista, order a drink and a snack in {lang['name']}, and ask how much it costs.",
            "opening_line": s0["dialogue_prompt"],
            "opening_line_en": s0["dialogue_prompt_en"],
            "suggested_replies": [
                s0["target"],
                pack["vocab"][0]["word"] + ", " + pack["vocab"][1]["word"],
                pack["sentences"][-1]["target"],
            ],
        },
        {
            "id": f"{lang_code}_rp_station",
            "title": f"Central Express Rail Desk ({lang['native_name']})",
            "location": "Main High-Speed Rail Terminal",
            "cefr": "CEFR A1–A2",
            "xp_reward": 45,
            "npc_name": "Inspector Elena",
            "npc_avatar": "👩🏻‍✈️",
            "objective": f"Ask where the platform or station is and request tickets to your destination in {lang['name']}.",
            "opening_line": s1["dialogue_prompt"],
            "opening_line_en": s1["dialogue_prompt_en"],
            "suggested_replies": [
                s1["target"],
                s0["target"],
            ],
        },
    ]


ALPHABET_DATA: Dict[str, List[Dict[str, Any]]] = {
    "ja": [
        {"char": "あ", "romaji": "a", "ipa": "/ä/", "type": "Hiragana Vowel", "example": "あさ (asa - morning)", "strokes": ["M 25 35 H 75", "M 50 18 V 82", "M 68 42 C 58 75, 25 82, 24 62 C 23 44, 65 38, 76 62 C 82 74, 72 86, 58 88"]},
        {"char": "い", "romaji": "i", "ipa": "/i/", "type": "Hiragana Vowel", "example": "いぬ (inu - dog)", "strokes": ["M 32 25 C 28 55, 32 76, 44 82", "M 68 30 C 74 48, 74 66, 68 78"]},
        {"char": "う", "romaji": "u", "ipa": "/ɯ/", "type": "Hiragana Vowel", "example": "うみ (umi - sea)", "strokes": ["M 40 20 L 62 26", "M 30 44 C 55 34, 76 46, 70 68 C 66 82, 48 88, 34 86"]},
        {"char": "え", "romaji": "e", "ipa": "/e/", "type": "Hiragana Vowel", "example": "えき (eki - station)", "strokes": ["M 42 20 L 62 24", "M 26 42 H 72 L 32 78 C 46 62, 62 64, 78 82"]},
        {"char": "お", "romaji": "o", "ipa": "/o/", "type": "Hiragana Vowel", "example": "おちゃ (ocha - tea)", "strokes": ["M 26 36 H 64", "M 46 18 V 80 C 32 82, 22 70, 28 58 C 36 46, 68 48, 72 68 C 74 80, 64 86, 54 86", "M 74 26 L 82 34"]},
        {"char": "か", "romaji": "ka", "ipa": "/kä/", "type": "Hiragana K-row", "example": "かさ (kasa - umbrella)", "strokes": ["M 22 42 H 60 C 58 68, 52 82, 40 84", "M 42 20 L 30 82", "M 72 34 L 82 58"]},
        {"char": "き", "romaji": "ki", "ipa": "/kʲi/", "type": "Hiragana K-row", "example": "きっぷ (kippu - ticket)", "strokes": ["M 28 32 H 68", "M 26 48 H 70", "M 50 18 L 58 64", "M 32 72 C 42 86, 62 88, 74 82"]},
        {"char": "く", "romaji": "ku", "ipa": "/kɯ/", "type": "Hiragana K-row", "example": "くるま (kuruma - car)", "strokes": ["M 64 20 L 32 52 L 66 84"]},
        {"char": "け", "romaji": "ke", "ipa": "/ke/", "type": "Hiragana K-row", "example": "けさ (kesa - this morning)", "strokes": ["M 28 24 C 24 52, 26 72, 34 82", "M 46 40 H 78", "M 64 20 C 64 56, 58 76, 44 86"]},
        {"char": "こ", "romaji": "ko", "ipa": "/ko/", "type": "Hiragana K-row", "example": "ここ (koko - here)", "strokes": ["M 30 30 H 70", "M 28 68 C 38 82, 62 82, 74 74"]},
        {"char": "ア", "romaji": "a (Katakana)", "ipa": "/ä/", "type": "Katakana Vowel", "example": "アメリカ (Amerika)", "strokes": ["M 26 28 H 76 L 52 54", "M 52 44 C 50 66, 42 78, 28 86"]},
        {"char": "カ", "romaji": "ka (Katakana)", "ipa": "/kä/", "type": "Katakana K-row", "example": "カメラ (kamera - camera)", "strokes": ["M 24 38 H 72 C 70 66, 64 80, 52 84", "M 50 18 C 48 52, 38 74, 24 86"]},
    ],
    "ko": [
        {"char": "ㄱ", "romaji": "g / k", "ipa": "/k ~ ɡ/", "type": "Hangul Consonant", "example": "가방 (gabang - bag)", "strokes": ["M 26 28 H 74 V 78"]},
        {"char": "ㄴ", "romaji": "n", "ipa": "/n/", "type": "Hangul Consonant", "example": "나무 (namu - tree)", "strokes": ["M 28 24 V 74 H 76"]},
        {"char": "ㄷ", "romaji": "d / t", "ipa": "/t ~ d/", "type": "Hangul Consonant", "example": "도시 (dosi - city)", "strokes": ["M 28 26 H 74", "M 28 26 V 76 H 76"]},
        {"char": "ㄹ", "romaji": "r / l", "ipa": "/ɾ ~ l/", "type": "Hangul Consonant", "example": "라면 (ramyeon)", "strokes": ["M 26 24 H 72 V 48", "M 26 48 H 72", "M 26 48 V 76 H 74"]},
        {"char": "ㅁ", "romaji": "m", "ipa": "/m/", "type": "Hangul Consonant", "example": "물 (mul - water)", "strokes": ["M 28 26 V 76", "M 28 26 H 72 V 76", "M 28 76 H 72"]},
        {"char": "ㅂ", "romaji": "b / p", "ipa": "/p ~ b/", "type": "Hangul Consonant", "example": "밥 (bap - rice)", "strokes": ["M 28 24 V 76", "M 72 24 V 76", "M 28 50 H 72", "M 28 76 H 72"]},
        {"char": "ㅅ", "romaji": "s", "ipa": "/s/", "type": "Hangul Consonant", "example": "사랑 (sarang - love)", "strokes": ["M 52 24 L 24 78", "M 48 44 L 76 78"]},
        {"char": "ㅇ", "romaji": "silent / -ng", "ipa": "/∅ ~ ŋ/", "type": "Hangul Consonant", "example": "안녕 (annyeong - hello)", "strokes": ["M 50 24 C 72 24, 78 76, 50 76 C 22 76, 28 24, 50 24"]},
        {"char": "ㅏ", "romaji": "a", "ipa": "/ɐ/", "type": "Hangul Vowel", "example": "아침 (achim - morning)", "strokes": ["M 44 18 V 84", "M 44 50 H 74"]},
        {"char": "ㅓ", "romaji": "eo", "ipa": "/ʌ/", "type": "Hangul Vowel", "example": "커피 (keopi - coffee)", "strokes": ["M 26 50 H 56", "M 56 18 V 84"]},
        {"char": "ㅗ", "romaji": "o", "ipa": "/o/", "type": "Hangul Vowel", "example": "오늘 (oneul - today)", "strokes": ["M 50 26 V 58", "M 20 58 H 80"]},
        {"char": "ㅜ", "romaji": "u", "ipa": "/u/", "type": "Hangul Vowel", "example": "우유 (uyu - milk)", "strokes": ["M 20 40 H 80", "M 50 40 V 76"]},
    ],
    "zh": [
        {"char": "水", "romaji": "shuǐ (3rd tone)", "ipa": "water", "type": "Hanzi Radical", "example": "喝水 (hē shuǐ - drink water)", "strokes": ["M 50 18 V 82 L 38 72", "M 22 46 H 42 L 22 74", "M 76 34 L 54 52 L 80 76"]},
        {"char": "人", "romaji": "rén (2nd tone)", "ipa": "person", "type": "Hanzi Radical", "example": "中国人 (Zhōngguórén)", "strokes": ["M 54 20 L 22 80", "M 46 42 L 80 80"]},
        {"char": "大", "romaji": "dà (4th tone)", "ipa": "big / great", "type": "Hanzi Character", "example": "大学 (dàxué - university)", "strokes": ["M 20 44 H 80", "M 50 18 C 48 54, 36 74, 20 84", "M 50 46 L 80 84"]},
        {"char": "口", "romaji": "kǒu (3rd tone)", "ipa": "mouth / opening", "type": "Hanzi Radical", "example": "出口 (chūkǒu - exit)", "strokes": ["M 28 28 V 74", "M 28 28 H 72 V 74", "M 28 74 H 72"]},
        {"char": "日", "romaji": "rì (4th tone)", "ipa": "sun / day", "type": "Hanzi Radical", "example": "今日 (jīnrì - today)", "strokes": ["M 30 22 V 80", "M 30 22 H 70 V 80", "M 30 50 H 70", "M 30 80 H 70"]},
        {"char": "中", "romaji": "zhōng (1st tone)", "ipa": "middle / center", "type": "Hanzi Character", "example": "中文 (Zhōngwén - Chinese)", "strokes": ["M 24 36 V 62", "M 24 36 H 76 V 62", "M 24 62 H 76", "M 50 14 V 88"]},
    ],
    "ru": [
        {"char": "А", "romaji": "a", "ipa": "/a/", "type": "Cyrillic Vowel", "example": "автобус (avtobus - bus)", "strokes": ["M 50 20 L 24 80", "M 50 20 L 76 80", "M 34 58 H 66"]},
        {"char": "Б", "romaji": "b", "ipa": "/b/", "type": "Cyrillic Consonant", "example": "билет (bilet - ticket)", "strokes": ["M 30 22 V 80", "M 30 22 H 72", "M 30 50 H 66 C 78 50, 78 80, 66 80 H 30"]},
        {"char": "Д", "romaji": "d", "ipa": "/d/", "type": "Cyrillic Consonant", "example": "дом (dom - house)", "strokes": ["M 40 24 L 30 70", "M 40 24 H 66 V 70", "M 22 70 H 78", "M 22 70 V 84", "M 78 70 V 84"]},
        {"char": "Ж", "romaji": "zh", "ipa": "/ʐ/", "type": "Cyrillic Consonant", "example": "журнал (zhurnal)", "strokes": ["M 24 24 L 50 52 L 24 80", "M 50 20 V 84", "M 76 24 L 50 52 L 76 80"]},
        {"char": "П", "romaji": "p", "ipa": "/p/", "type": "Cyrillic Consonant", "example": "паспорт (pasport)", "strokes": ["M 28 24 V 80", "M 28 24 H 72 V 80"]},
        {"char": "Я", "romaji": "ya", "ipa": "/ja/", "type": "Cyrillic Vowel", "example": "яблоко (yabloko - apple)", "strokes": ["M 68 22 V 82", "M 68 22 H 38 C 24 22, 24 52, 38 52 H 68", "M 46 52 L 26 82"]},
    ],
    "ar": [
        {"char": "ا", "romaji": "ʾalif (ā)", "ipa": "/aː/", "type": "Arabic Letter", "example": "أنا (anā - I)", "strokes": ["M 50 18 V 82"]},
        {"char": "ب", "romaji": "bāʾ (b)", "ipa": "/b/", "type": "Arabic Letter", "example": "باب (bāb - door)", "strokes": ["M 76 44 V 64 H 24 V 44", "M 50 78 L 52 80"]},
        {"char": "ت", "romaji": "tāʾ (t)", "ipa": "/t/", "type": "Arabic Letter", "example": "تفاح (tuffāḥ - apple)", "strokes": ["M 76 48 V 68 H 24 V 48", "M 44 34 L 46 36", "M 56 34 L 58 36"]},
        {"char": "ج", "romaji": "jīm (j)", "ipa": "/dʒ/", "type": "Arabic Letter", "example": "جبن (jubn - cheese)", "strokes": ["M 28 30 H 72 L 38 54 C 24 68, 42 86, 68 80", "M 52 66 L 54 68"]},
        {"char": "ش", "romaji": "shīn (sh)", "ipa": "/ʃ/", "type": "Arabic Letter", "example": "شاي (shāy - tea)", "strokes": ["M 78 48 V 64 H 62 V 48 V 64 H 46 V 48 V 64 C 46 80, 22 80, 22 58", "M 54 26 L 56 28", "M 48 34 L 50 36", "M 60 34 L 62 36"]},
        {"char": "م", "romaji": "mīm (m)", "ipa": "/m/", "type": "Arabic Letter", "example": "ماء (māʾ - water)", "strokes": ["M 56 44 C 70 44, 70 60, 56 60 C 42 60, 42 44, 56 44 H 32 V 84"]},
    ],
}


def get_alphabet_for_language(lang_code: str) -> List[Dict[str, Any]]:
    """Returns character/phonetics cards + stroke paths for the selected language."""
    if lang_code in ALPHABET_DATA:
        return ALPHABET_DATA[lang_code]
    # For Latin-script languages (es, fr, de, it, pt), provide accented & phonetic letter mastery cards
    lang = LANGUAGES.get(lang_code, LANGUAGES["es"])
    pack = LANGUAGE_PACKS.get(lang_code, LANGUAGE_PACKS["es"])
    cards = []
    for idx, acc in enumerate(lang["accents"][:8]):
        sample_v = pack["vocab"][idx % len(pack["vocab"])]
        cards.append(
            {
                "char": acc,
                "romaji": f"{lang['name']} Special Character",
                "ipa": f"/{acc}/",
                "type": lang["script_name"],
                "example": f"{sample_v['word']} ({sample_v['translation']})",
                "strokes": [
                    "M 60 20 L 44 34",
                    "M 32 58 C 32 42, 68 42, 68 58 V 80 C 50 84, 30 80, 32 64 C 34 52, 64 54, 68 64",
                ],
            }
        )
    return cards


SHOP_ITEMS: List[Dict[str, Any]] = [
    {
        "id": "heart_refill",
        "name": "Full Heart Refill",
        "description": "Restore all 5 Hearts immediately so you can keep learning without interruption.",
        "cost": 350,
        "icon": "❤️",
        "category": "Hearts",
    },
    {
        "id": "streak_freeze",
        "name": "Streak Freeze",
        "description": "Protects your daily 🔥 streak for 1 full day of inactivity (Max 2 equipped).",
        "cost": 200,
        "icon": "🧊",
        "category": "Power-Ups",
    },
    {
        "id": "xp_boost_15m",
        "name": "Double XP Potion (2x XP)",
        "description": "Earn 2x XP on every lesson, Story, and AI Roleplay for the next 15 minutes!",
        "cost": 150,
        "icon": "⚡",
        "category": "Boosts",
    },
    {
        "id": "duolingo_max_pass",
        "name": "Duolingo Max Pass (Unlimited Hearts + AI)",
        "description": "Unlock Unlimited ∞ Hearts, Explain My Answer AI, and Live AI Roleplay Missions.",
        "cost": 500,
        "icon": "👑",
        "category": "Duolingo Max",
    },
]
