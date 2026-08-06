import os
import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def safe_delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result
