import logging

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message, exc_info=True):
        self.logger.exception(message, exc_info=exc_info)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_critical(self, message):
        self.logger.critical(message)  

if __name__ == '__main__':
    log = Logger(__name__)
    log.log_info('This is an info log')
    log.log_warning('This is a warning log')
    log.log_error('This is an error log')
    log.log_debug('This is a debug log')
    log.log_critical('This is a critical log')
    try:
        1 / 0
    except ZeroDivisionError:
        log.log_exception('Division by zero error occurred')