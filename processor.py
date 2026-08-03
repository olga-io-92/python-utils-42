import json

class Processor:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance(self.data, dict):
            raise ValueError('Input must be a dictionary')
        if 'input_value' not in self.data:
            raise KeyError('Key `input_value` is required')
        if not isinstance(self.data['input_value'], (int, float)):
            raise TypeError('Value of `input_value` must be a number')

    def process(self):
        self.validate_input()
        result = self.data['input_value'] * 2
        return json.dumps({'result': result})

if __name__ == '__main__':
    input_data = {'input_value': 5}
    processor = Processor(input_data)
    try:
        output = processor.process()
        print(output)
    except (ValueError, KeyError, TypeError) as e:
        print(f'Error: {e}')