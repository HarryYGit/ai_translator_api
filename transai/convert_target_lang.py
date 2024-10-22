ACCEPT_LANGUAGE_TO_TRANSLATOR_FORMAT = {
    'en-US': 'eng_Latn',  # English (United States)
    'en-GB': 'eng_Latn',  # English (United Kingdom)
    'zh-CN': 'zho_Hans',  # Simplified Chinese
    'zh-TW': 'zho_Hant',  # Traditional Chinese (Taiwan)
    'fr-FR': 'fra_Latn',  # French (France)
    'fr-CA': 'fra_Latn',  # French (Canada)
    'es-ES': 'spa_Latn',  # Spanish (Spain)
    'es-MX': 'spa_Latn',  # Spanish (Mexico)
    'de-DE': 'deu_Latn',  # German (Germany)
    'it-IT': 'ita_Latn',  # Italian (Italy)
    'pt-PT': 'por_Latn',  # Portuguese (Portugal)
    'pt-BR': 'por_Latn',  # Portuguese (Brazil)
    'ja-JP': 'jpn_Jpan',  # Japanese
    'ko-KR': 'kor_Hang',  # Korean
    'ru-RU': 'rus_Cyrl',  # Russian
    'ar-SA': 'ara_Arab',  # Arabic (Saudi Arabia)
    'hi-IN': 'hin_Deva',  # Hindi (India)
    'bn-BD': 'ben_Beng',  # Bengali (Bangladesh)
    'fa-IR': 'pes_Arab',  # Persian (Iran)
    'tr-TR': 'tur_Latn',  # Turkish (Turkey)
    'nl-NL': 'nld_Latn',  # Dutch (Netherlands)
    'pl-PL': 'pol_Latn',  # Polish (Poland)
    'th-TH': 'tha_Thai',  # Thai (Thailand)
    'vi-VN': 'vie_Latn',  # Vietnamese (Vietnam)
    'he-IL': 'heb_Hebr',  # Hebrew (Israel)
    'el-GR': 'ell_Grek',  # Greek (Greece)
    'sv-SE': 'swe_Latn',  # Swedish (Sweden)
    'uk-UA': 'ukr_Cyrl',  # Ukrainian
    'fi-FI': 'fin_Latn',  # Finnish (Finland)
    'no-NO': 'nor_Latn',  # Norwegian (Norway)
    'da-DK': 'dan_Latn',  # Danish (Denmark)
    'cs-CZ': 'ces_Latn',  # Czech (Czech Republic)
    'hu-HU': 'hun_Latn',  # Hungarian (Hungary)
    'ro-RO': 'ron_Latn',  # Romanian (Romania)
    'bg-BG': 'bul_Cyrl',  # Bulgarian (Bulgaria)
    # Add more as needed
}

def convert_to_accept(accept_language):
    return ACCEPT_LANGUAGE_TO_TRANSLATOR_FORMAT.get(accept_language, 'eng_Latn')