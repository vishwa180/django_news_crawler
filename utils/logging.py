import logging


def get_default_logger():
    logger = logging.getLogger('default_logger')
    return logger


def get_exception_logger():
    logger = logging.getLogger('exception_logger')
    return logger
