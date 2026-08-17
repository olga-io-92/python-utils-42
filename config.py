import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.default_config.copy()

    def load_from_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_config = json.load(f)
            self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Usage:
# default_config = {'setting1': 'default_value', 'setting2': 42}
# config_loader = ConfigLoader(default_config)
# config_loader.load_from_file('config.json')
# value = config_loader.get('setting1')
