import json

class InputValidationError(Exception):
    pass

def process_input(user_input):
    if not isinstance(user_input, str) or not user_input:
        raise InputValidationError('Input must be a non-empty string.')