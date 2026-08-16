import json
from typing import Any, Dict

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    return {**dict1, **dict2}


def filter_keys(data: Dict[str, Any], keys: set) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if k in keys}
