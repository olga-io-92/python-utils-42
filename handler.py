import json
from typing import Any, Dict, List, Union

def normalize_data(data: Union[Dict[str, Any], List[Any]]) -> Dict[str, Any]:
    if isinstance(data, list):
        return {str(i): item for i, item in enumerate(data)}
    elif isinstance(data, dict):
        return {key: value for key, value in data.items()}
    return {}


def save_to_json(data: Union[Dict[str, Any], List[Any]], filename: str) -> None:
    normalized_data = normalize_data(data)
    with open(filename, 'w') as f:
        json.dump(normalized_data, f, ensure_ascii=False, indent=4)


def load_from_json(filename: str) -> Union[Dict[str, Any], List[Any]]:
    with open(filename, 'r') as f:
        return json.load(f)