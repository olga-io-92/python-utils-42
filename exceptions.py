class DataError(Exception):
    pass

class NotFoundError(DataError):
    def __init__(self, message):
        super().__init__(f'Not Found: {message}')

class ValidationError(DataError):
    def __init__(self, message):
        super().__init__(f'Validation Error: {message}')

class DatabaseError(DataError):
    def __init__(self, message):
        super().__init__(f'Database Error: {message}')

class NetworkError(DataError):
    def __init__(self, message):
        super().__init__(f'Network Error: {message}')

class TimeoutError(DataError):
    def __init__(self, message):
        super().__init__(f'Timeout Error: {message}')