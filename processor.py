from typing import List, Dict


def process_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Processes a list of data dictionaries.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries containing data to be processed.

    Returns:
        List[Dict[str, str]]: A list of processed data dictionaries.
    """
    processed = []
    for item in data:
        # Example processing: convert all values to uppercase
        processed_item = {k: v.upper() for k, v in item.items()}
        processed.append(processed_item)
    return processed


def validate_data(data: List[Dict[str, str]]) -> bool:
    """
    Validates the input data format.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries containing data to validate.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, dict):
            return False
    return True
