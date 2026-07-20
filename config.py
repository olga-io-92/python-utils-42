import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.configuration = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Config file {self.config_file} not found.')
        
        try:
            with open(self.config_file, 'r') as file:
                config_data = json.load(file)
        except json.JSONDecodeError:
            raise ConfigError('Invalid JSON format in config file.')
        
        if not isinstance(config_data, dict):
            raise ConfigError('Config must be a JSON object.')
        
        return config_data

    def get(self, key, default=None):
        return self.configuration.get(key, default)  
