import json

def process_data(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    return {key: value for key, value in data.items() if value is not None}


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main(file_path):
    data = read_json(file_path)
    cleaned_data = process_data(data)
    write_json(file_path, cleaned_data)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python processor.py <file_path>')
        sys.exit(1)
    main(sys.argv[1])