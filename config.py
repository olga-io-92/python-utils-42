import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.default_config.copy()

    def load(self, filepath):
        if Path(filepath).is_file():
            with open(filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.config, file, indent=4)