from typing import List, Dict, Any


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary.

    Args:
        d (Dict[str, Any]): The dictionary to flatten.
        parent_key (str, optional): The base key string.
        sep (str, optional): Separator to use between keys.

    Returns:
        Dict[str, Any]: A new flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unique_list(seq: List[Any]) -> List[Any]:
    """Return a list of unique elements while preserving order.

    Args:
        seq (List[Any]): The input list from which to get unique elements.

    Returns:
        List[Any]: A list of unique elements.
    """
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def deep_merge(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries deeply.

    Args:
        a (Dict[str, Any]): The first dictionary.
        b (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: A new dictionary containing the merged keys and values.
    """
    for k, v in b.items():
        if isinstance(v, dict) and k in a:
            a[k] = deep_merge(a[k], v)
        else:
            a[k] = v
    return a