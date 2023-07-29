from googletrans import Translator, LANGUAGES

def get_supported_languages():
    return LANGUAGES

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, src=source_lang, dest=target_lang)
        return translation.text
    except Exception as e:
        return f"Translation error: {e}"

if __name__ == "__main__":
    print("Supported languages:")
    for code, language in get_supported_languages().items():
        print(f"{code}: {language}")

    source_language = input("Enter the source language code (e.g., en): ")
    target_language = input("Enter the target language code (e.g., fr): ")
    text_to_translate = input("Enter the text to translate: ")

    translated_text = translate_text(text_to_translate, source_language, target_language)
    print(f"Translated text: {translated_text}")
