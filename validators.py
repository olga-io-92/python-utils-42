from typing import Any, Dict, List, Union


def validate_string(value: Any) -> bool:
    """
    Validates if the input is a non-empty string.

    Args:
        value (Any): The value to be checked.

    Returns:
        bool: True if value is a non-empty string, False otherwise.
    """
    return isinstance(value, str) and bool(value)


def validate_integer(value: Any) -> bool:
    """
    Validates if the input is an integer.

    Args:
        value (Any): The value to be checked.

    Returns:
        bool: True if value is an integer, False otherwise.
    """
    return isinstance(value, int)


def validate_list_of_strings(value: Any) -> bool:
    """
    Validates if the input is a list of non-empty strings.

    Args:
        value (Any): The value to be checked.

    Returns:
        bool: True if value is a list of non-empty strings, False otherwise.
    """
    return isinstance(value, list) and all(validate_string(item) for item in value)


def validate_dict(value: Any) -> bool:
    """
    Validates if the input is a dictionary.

    Args:
        value (Any): The value to be checked.

    Returns:
        bool: True if value is a dictionary, False otherwise.
    """
    return isinstance(value, dict)


def validate_date_format(value: str) -> bool:
    """
    Validates if the input string matches the format 'YYYY-MM-DD'.

    Args:
        value (str): The date string to be checked.

    Returns:
        bool: True if the value matches the date format, False otherwise.
    """
    import re
    date_pattern = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
    return bool(date_pattern.match(value))
