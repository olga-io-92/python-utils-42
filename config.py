import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def update(self, updates):
        self.config.update(updates)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    print(loader.get('some_key', 'default_value'))