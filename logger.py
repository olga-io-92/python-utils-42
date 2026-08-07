import logging


def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(ch)
    return logger


def log_exception(logger, exception):
    logger.exception('An error occurred: %s', exception)


def log_message(logger, message):
    logger.info(message)


def log_warning(logger, message):
    logger.warning(message)