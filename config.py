import json
import os

def load_config(file_path):
    if not isinstance(file_path, str):
        raise ValueError('File path must be a string')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'Config file not found: {file_path}')
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON format')
    return config


def save_config(file_path, data):
    if not isinstance(file_path, str):
        raise ValueError('File path must be a string')
    if not isinstance(data, dict):
        raise ValueError('Data must be a dictionary')
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise Exception(f'An error occurred while writing to the file: {e}')