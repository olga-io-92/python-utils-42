import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flat_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def filter_dict(data_dict, keys):
    return {key: data_dict[key] for key in keys if key in data_dict}
