from typing import List, Any

def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (List[List[Any]]): A list of lists to flatten.

    Returns:
        List[Any]: A single list containing all elements of the nested lists.
    """
    return [item for sublist in nested_list for item in sublist]


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Splits a list into chunks of a specified size.

    Args:
        data (List[Any]): The list to split into chunks.
        chunk_size (int): The size of each chunk.

    Returns:
        List[List[Any]]: A list of lists, each containing a chunk of the original list.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries into one.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A dictionary containing keys and values from both dictionaries.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged
