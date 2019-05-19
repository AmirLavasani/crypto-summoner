import logging


INTELI_LOGGER_LOG_LEVEL = logging.DEBUG

INTELI_LOGGER_STREAM_LOGGING_LEVEL = logging.DEBUG
INTELI_LOGGER_STREAM_FORMAT = '%(process)d - %(asctime)s - %(log_color)s%(name)s%(reset)s - %(log_color)s%(levelname)-8s%(reset)s - %(log_color)s%(message)s%(reset)s'

INTELI_LOGGER_FILE_LOGGING_LEVEL = logging.DEBUG
INTELI_LOGGER_FILE_FORMAT = '%(name)s - %(levelname)s - %(message)s'

INTELI_LOGGER_LOG_FILE = '/tmp/inteli_logger.log'