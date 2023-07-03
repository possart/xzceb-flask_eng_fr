"""module to translate EN & french languages"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    method used to translated a english string to french.
    """
    try:
        mem_translator = MyMemoryTranslator("en-GB", "fr-FR")
        french_text = mem_translator.translate(english_text)
    except Exception:
        print("This is not english.")

    return french_text

def french_to_english (french_text):
    """
    method used to translated a english string to french.
    """
    try:
        mem_translator = MyMemoryTranslator("fr-FR","en-GB")
        english_text = mem_translator.translate(french_text)
    except Exception:
        print("This is not french.")

    return english_text
