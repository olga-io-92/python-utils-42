import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list_of_dicts(list_of_dicts):
    return [item for d in list_of_dicts for item in d.items()]


def filter_dict(data, keys):
    return {key: data[key] for key in keys if key in data}