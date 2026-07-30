class CustomException(Exception):
    pass

class ValidationException(CustomException):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class NotFoundException(CustomException):
    pass

class PermissionException(CustomException):
    def __init__(self, message):
        super().__init__(message)

class DatabaseException(CustomException):
    pass

class NetworkException(CustomException):
    pass

class ResourceConflictException(CustomException):
    def __init__(self, resource):
        super().__init__(f'Resource conflict with {resource}')
