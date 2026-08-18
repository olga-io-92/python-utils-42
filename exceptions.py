class CustomError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class NotFoundError(CustomError):
    def __init__(self, resource):
        super().__init__(f'{resource} not found', code=404)

class ValidationError(CustomError):
    def __init__(self, field, message):
        super().__init__(f'Validation error on {field}: {message}', code=400)

class AuthenticationError(CustomError):
    def __init__(self):
        super().__init__('Authentication failed', code=401)

class PermissionError(CustomError):
    def __init__(self):
        super().__init__('Permission denied', code=403)

class DatabaseError(CustomError):
    def __init__(self, operation):
        super().__init__(f'Database operation failed: {operation}', code=500)