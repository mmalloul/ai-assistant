import json
import os

class TextManager:
    def __init__(self, language='en'):
        self.language = language
        self.text_data = self.load_text_data()

    def load_text_data(self):
        lang_path = os.path.join('lang', f'{self.language}.json')
        try:
            with open(lang_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Language file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON from language file.")
            return {}

    def get_text(self, category, key):
        return self.text_data.get(category, {}).get(key, f"[{category}.{key} not found]")

