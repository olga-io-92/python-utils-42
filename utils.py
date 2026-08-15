import json

class CustomError(Exception):
    pass

def safe_load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise CustomError(f'File not found: {file_path}')
    except json.JSONDecodeError:
        raise CustomError('Invalid JSON format')
    except Exception as e:
        raise CustomError(f'Unexpected error: {str(e)}')

def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        raise CustomError('Cannot divide by zero')
    except TypeError:
        raise CustomError('Both numerator and denominator must be numbers')
    except Exception as e:
        raise CustomError(f'Unexpected error: {str(e)}')

def read_and_process_json(file_path):
    data = safe_load_json(file_path)
    return data

def main():
    file_path = 'data.json'
    try:
        data = read_and_process_json(file_path)
        result = divide_numbers(data['value'], data['divisor'])
        print(result)
    except CustomError as e:
        print(e)

if __name__ == '__main__':
    main()