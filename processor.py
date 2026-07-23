import json
from validators import validate_input

def process_data(input_data):
    if not validate_input(input_data):
        raise ValueError('Invalid input data')
    result = {}  # Process the input data here
    # Example processing (mock)
    result['output'] = input_data.upper()  # Simple transformation example
    return result

def main():
    data = input('Enter some data: ')
    try:
        output = process_data(data)
        print(json.dumps(output, indent=2))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()