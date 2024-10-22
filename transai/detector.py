from langdetect import detect

def detect_lang(input):
    
    lang = detect(input)

    return lang


