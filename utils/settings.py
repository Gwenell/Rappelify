import json
import os

class Settings:
    def __init__(self):
        self.settings_file = 'settings.json'
        self.default_settings = {
            'language': 'en',
            'theme': 'light',
            'custom_colors': {
                'primary': '#FFFFFF',
                'secondary': '#000000'
            }
        }
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                loaded_settings = json.load(f)
                return {**self.default_settings, **loaded_settings}
        return self.default_settings.copy()

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def get_all(self):
        return self.settings

    def set_all(self, new_settings):
        self.settings = {**self.default_settings, **new_settings}
        self.save_settings()

settings = Settings()