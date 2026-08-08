class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class NotFoundError(Exception):
    def __init__(self, resource: str):
        message = f'{resource} not found'
        super().__init__(message)
        self.resource = resource

class PermissionDeniedError(Exception):
    def __init__(self, action: str):
        message = f'Permission denied for {action}'
        super().__init__(message)
        self.action = action

class DatabaseError(Exception):
    def __init__(self, db_message: str):
        message = f'Database error: {db_message}'
        super().__init__(message)
        self.db_message = db_message
