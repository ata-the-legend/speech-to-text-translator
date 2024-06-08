

from deep_translator import GoogleTranslator
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def english_to_farsi(etext):
    try:
        translator = GoogleTranslator(source='en', target='fa')
        translated_text = translator.translate(etext)
        return translated_text
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Error: {e}")
        logging.error("There was a problem connecting to the translation service. Please check your network connection and try again.")

