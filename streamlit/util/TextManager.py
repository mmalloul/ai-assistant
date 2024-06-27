import json

class TextManager:
    def __init__(self, language: str):
        with open(f'lang/{language}.json', 'r') as f:
            self.texts = json.load(f)

    def get_text(self, category: str, key: str) -> str:
        return self.texts.get(category, {}).get(key, '')