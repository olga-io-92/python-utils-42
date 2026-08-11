import os

class Constants:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    LOGGING_LEVEL = 'DEBUG'
    MAX_RETRIES = 5
    TIMEOUT = 30
    API_URL = 'https://api.example.com'
    RESPONSE_FORMAT = 'json'
    FILE_EXTENSIONS = ['.txt', '.csv', '.json']
    BUFFER_SIZE = 4096
    ENCODING = 'utf-8'

constants = Constants()