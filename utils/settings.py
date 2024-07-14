import json
import os

class Settings:
    def __init__(self):
        self.settings_file = 'settings.json'
        self.default_settings = {
            'language': 'en',  # Default language setting
            'theme': 'light',  # Default theme setting
            'custom_colors': {
                'primary': '#FFFFFF',  # Default primary color
                'secondary': '#000000'  # Default secondary color
            }
        }
        self.settings = self.load_settings()  # Load settings from file or use defaults

    def load_settings(self):
        """
        Load settings from the settings file. If the file exists, merge its
        contents with the default settings. Otherwise, return a copy of the
        default settings.
        """
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                loaded_settings = json.load(f)
                return {**self.default_settings, **loaded_settings}
        return self.default_settings.copy()

    def save_settings(self):
        """
        Save the current settings to the settings file in JSON format.
        """
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f)

    def get(self, key, default=None):
        """
        Retrieve a value from the settings using the given key. If the key
        does not exist, return the provided default value.
        """
        return self.settings.get(key, default)

    def set(self, key, value):
        """
        Set a value in the settings for the given key and save the updated
        settings to the file.
        """
        self.settings[key] = value
        self.save_settings()

    def get_all(self):
        """
        Return all settings as a dictionary.
        """
        return self.settings

    def set_all(self, new_settings):
        """
        Replace all current settings with the provided new settings,
        merging them with the default settings, and save the updated
        settings to the file.
        """
        self.settings = {**self.default_settings, **new_settings}
        self.save_settings()

# Initialize the settings instance
settings = Settings()
