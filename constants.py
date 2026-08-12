from typing import Final

# Constants used throughout the application

PI: Final[float] = 3.14159
EULER: Final[float] = 2.71828

STATUS_ACTIVE: Final[str] = 'active'
STATUS_INACTIVE: Final[str] = 'inactive'
STATUS_PENDING: Final[str] = 'pending'

MAX_RETRIES: Final[int] = 5
TIMEOUT: Final[int] = 30

# HTTP status codes
HTTP_OK: Final[int] = 200
HTTP_NOT_FOUND: Final[int] = 404
HTTP_SERVER_ERROR: Final[int] = 500

# File paths
LOG_FILE_PATH: Final[str] = '/var/log/app.log'
DATA_FILE_PATH: Final[str] = '/data/input.json'

# Define user roles
ROLE_ADMIN: Final[str] = 'admin'
ROLE_USER: Final[str] = 'user'
ROLE_GUEST: Final[str] = 'guest'