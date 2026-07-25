class CustomError(Exception):
    pass

class ValidationError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class NotFoundError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class PermissionError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class DatabaseError(CustomError):
    def __init__(self, message):
        super().__init__(message)

class ConfigurationError(CustomError):
    def __init__(self, message):
        super().__init__(message)