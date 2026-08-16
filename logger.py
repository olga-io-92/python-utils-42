import logging
import os

class Logger:
    def __init__(self, log_file='app.log', level=logging.INFO):
        if not isinstance(log_file, str) or not log_file:
            raise ValueError('log_file must be a non-empty string')
        self.log_file = log_file
        self.level = level
        self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(
            filename=self.log_file,
            level=self.level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        if not os.access(os.path.dirname(self.log_file), os.W_OK):
            raise PermissionError(f'No write permission for log file directory: {self.log_file}')

    def log(self, message, level=None):
        if level is None:
            level = self.level
        if level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            raise ValueError('Invalid log level provided')
        logging.log(level, message)

    def set_level(self, level):
        if level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            raise ValueError('Invalid log level provided')
        self.level = level
        logging.getLogger().setLevel(level)