import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if not re.match('^[a-zA-Z0-9_]*$', user_input):
        raise ValueError('Input contains invalid characters. Only alphanumeric and underscores are allowed.')
    return True

def process_data(data):
    validate_input(data)
    # Process the validated input data
    return f'Processed: {data}'

def main():
    user_input = input('Enter some input: ')
    try:
        result = process_data(user_input)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()