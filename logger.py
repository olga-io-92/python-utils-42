import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message):
        self._log_with_error_handling(self.logger.debug, message)

    def info(self, message):
        self._log_with_error_handling(self.logger.info, message)

    def warning(self, message):
        self._log_with_error_handling(self.logger.warning, message)

    def error(self, message):
        self._log_with_error_handling(self.logger.error, message)

    def critical(self, message):
        self._log_with_error_handling(self.logger.critical, message)

    def _log_with_error_handling(self, log_method, message):
        try:
            if not isinstance(message, str):
                raise ValueError('Message must be a string')
            log_method(message)
        except Exception as e:
            self.logger.error(f'Logging failed: {str(e)}')