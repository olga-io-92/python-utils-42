class Handler:
    def __init__(self, data):
        self.data = data

    def process(self):
        try:
            result = self.validate(self.data)
            return self.transform(result)
        except ValueError as e:
            return {'error': str(e)}
        except TypeError:
            return {'error': 'Invalid type of input'}
        except Exception as e:
            return {'error': 'An unexpected error occurred: ' + str(e)}

    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError('Input must be a dictionary')
        if 'key' not in data:
            raise ValueError('Missing key in input data')
        return data

    def transform(self, data):
        return {k: v.upper() for k, v in data.items()}