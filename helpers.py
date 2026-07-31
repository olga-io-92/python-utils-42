from typing import Any, Dict


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary.

    Args:
        nested_dict (Dict[str, Any]): The dictionary to flatten.
        parent_key (str): The base key string for the keys in the flattened dictionary.
        sep (str): The separator to use for concatenated keys.

    Returns:
        Dict[str, Any]: A flattened dictionary.
    """
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_update(original: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively updates a dictionary with values from another dictionary.

    Args:
        original (Dict[str, Any]): The original dictionary to update.
        updates (Dict[str, Any]): The dictionary with updates.

    Returns:
        Dict[str, Any]: The updated dictionary.
    """
    for k, v in updates.items():
        if isinstance(v, dict) and k in original:
            original[k] = deep_update(original[k], v)
        else:
            original[k] = v
    return original


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges two dictionaries into one.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: The merged dictionary.
    """
    merged = dict(dict1)  # Copy dict1 to avoid modifying it
    merged.update(dict2)  # Update with dict2
    return merged
