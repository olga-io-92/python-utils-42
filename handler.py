import json

class InputError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InputError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise InputError('Missing or invalid name')
    if 'value' not in data or not isinstance(data['value'], (int, float)):
        raise InputError('Missing or invalid value')

def process_data(data):
    validate_input(data)
    result = data['value'] * 2  # Example processingeturn result

def main(input_json):
    try:
        data = json.loads(input_json)
        result = process_data(data)
        return json.dumps({'result': result})
    except InputError as e:
        return json.dumps({'error': str(e)})
    except json.JSONDecodeError:
        return json.dumps({'error': 'Invalid JSON'})

if __name__ == '__main__':
    sample_input = '{"name": "example", "value": 10}'
    print(main(sample_input))
