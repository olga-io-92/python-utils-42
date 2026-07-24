def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def one_hot_encode(labels):
    unique_labels = set(labels)
    label_to_index = {label: index for index, label in enumerate(unique_labels)}
    one_hot = [[0] * len(unique_labels) for _ in labels]
    for i, label in enumerate(labels):
        one_hot[i][label_to_index[label]] = 1
    return one_hot

import json

def save_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def generate_range(start, end, step=1):
    return list(range(start, end, step))
