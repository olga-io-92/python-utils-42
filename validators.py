class InputValidationError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, (int, float)):
        raise InputValidationError('Input must be a number.')
    if data < 0:
        raise InputValidationError('Input must be non-negative.')

class Processor:
    def process(self, input_data):
        try:
            validate_input(input_data)
            result = input_data ** 2  # Sample processing
            return result
        except InputValidationError as e:
            return str(e)

if __name__ == '__main__':
    processor = Processor()
    for value in [10, -5, 'a', 3.5]:
        output = processor.process(value)
        print(f'Input: {value}, Output: {output}')