import json
import logging

class CustomError(Exception):
    pass


def handle_request(data):
    if not isinstance(data, dict):
        raise CustomError('Invalid data format')
    try:
        response = process_data(data)
    except KeyError as e:
        raise CustomError(f'Missing key: {e}')
    except Exception as e:
        logging.error(f'Unhandled exception: {e}')
        raise CustomError('An unexpected error occurred')
    return response


def process_data(data):
    # Simulating data processing
    return json.dumps(data)

if __name__ == '__main__':
    sample_data = {'key': 'value'}  # Example data
    try:
        result = handle_request(sample_data)
        print(result)
    except CustomError as error:
        print(f'Error: {error}')