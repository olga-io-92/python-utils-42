import json


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_json_file(file_path, updates):
    data = load_json_file(file_path)
    data.update(updates)
    save_json_file(data, file_path)


def merge_json_files(file_paths, output_file):
    combined_data = {}
    for path in file_paths:
        data = load_json_file(path)
        combined_data.update(data)
    save_json_file(combined_data, output_file)