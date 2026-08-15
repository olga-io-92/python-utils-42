import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.user_config = {}

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        else:
            self.user_config = {}

    def get(self, key, default=None):
        return self.user_config.get(key, self.default_config.get(key, default))

    def set(self, key, value):
        self.user_config[key] = value

    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.user_config, file, indent=4)

# Example default configuration
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    config_loader.load('config.json')
    print(config_loader.get('host'))
    print(config_loader.get('port'))
