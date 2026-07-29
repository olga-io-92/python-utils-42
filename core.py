import json

class CustomError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise CustomError('Data should be a list.')
        self.data = data

    def process(self):
        try:
            return [self._process_item(item) for item in self.data]
        except Exception as e:
            raise CustomError(f'Processing error: {str(e)}')

    def _process_item(self, item):
        if not isinstance(item, dict):
            raise CustomError('Each item must be a dictionary.')
        if 'value' not in item:
            raise CustomError('Missing key: value')
        return item['value'] * 2

if __name__ == '__main__':
    try:
        data = json.loads('[{"value": 1}, {"value": 2}, {"value": 3}]')
        processor = DataProcessor(data)
        processed_data = processor.process()
        print(processed_data)
    except CustomError as e:
        print(f'Error: {e}')