import json


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def update_json(file_path, updates):
    data = load_json(file_path)
    data.update(updates)
    save_json(data, file_path)


def merge_json(file_path1, file_path2, output_path):
    data1 = load_json(file_path1)
    data2 = load_json(file_path2)
    merged_data = {**data1, **data2}
    save_json(merged_data, output_path)
