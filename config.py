import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        return self.config

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    loaded_config = config_loader.load('config.json')
    print(loaded_config)