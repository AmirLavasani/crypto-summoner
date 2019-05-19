"""
    InteliLogger is a class for customized logging.
    
    Any other class can log their activity using this class.
    
"""

import logging

from colorlog import ColoredFormatter

from crypto_summoner.inteli_logger.inteli_logger_conf import *


class InteliLogger:
    """
    InteliLogger Class

    InteliLogger is a class for customized logging.
    Any other class can log their activity using this class without getting into any logging details.

    ...

    Attributes:
        _registered_loggers (dic): Dictionary of initialized loggers.
    
    Methods:       
        get_logger(cls, logger_name): Returns the logger with logger_name.
        _add_stream_handler(cls, logger_name): Adds a stream handler to the logger with logger_name. 
        _add_file_handler(cls, logger_name): Adds a file handler to the logger with logger_name.
    """
    _registered_loggers = {}       

    @classmethod
    def get_logger(cls, logger_name):
        """
        Returns the logger with logger_name. 
        
        If the logger_name does not exists it creates the logger.
        If the logger_name exists in _registered_loggers it return the same object.

        By default it adds two handler to logger object. 
        A file handler which writes to INTELI_LOGGER_LOG_FILE path, and
        A stream handler which writes log to std_out.
               
        Args:
            logger_name (str): Name of the logger.            
        
        Returns:
            Returns a logging.Logger instance.        
        """

        if logger_name not in cls._registered_loggers.keys():
            cls._registered_loggers[logger_name] = logging.getLogger(logger_name)
            cls._registered_loggers[logger_name].setLevel(INTELI_LOGGER_LOG_LEVEL)
            cls._add_stream_handler(logger_name)
            cls._add_file_handler(logger_name)

        return cls._registered_loggers[logger_name]
    
    @classmethod
    def _add_stream_handler(cls, logger_name):
        """
        Add a logging.StreamHandler to the logger with logger_name

        Using ColoredFormatter from colorlog the stream output will be colored.      
               
        Args:
            logger_name (str): Name of the logger.            
        
        Returns:
            Returns nothing.        
        """

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(INTELI_LOGGER_STREAM_LOGGING_LEVEL)
        stream_format = ColoredFormatter(INTELI_LOGGER_STREAM_FORMAT)
        stream_handler.setFormatter(stream_format)        
        logger = cls._registered_loggers[logger_name]
        logger.addHandler(stream_handler)
    
    @classmethod
    def _add_file_handler(cls, logger_name):
        """
        Add a logging.FileHandler to the logger with logger_name        
               
        Args:
            logger_name (str): Name of the logger.            
        
        Returns:
            Returns nothing.        
        """

        file_handler = logging.FileHandler(INTELI_LOGGER_LOG_FILE)
        file_handler.setLevel(INTELI_LOGGER_FILE_LOGGING_LEVEL)
        stream_format = logging.Formatter(INTELI_LOGGER_FILE_FORMAT)
        file_handler.setFormatter(stream_format)
        logger = cls._registered_loggers[logger_name]
        logger.addHandler(file_handler)


def test_inteli_logger():
    log1 = InteliLogger.get_logger('log1')
    log2 = InteliLogger.get_logger('log2')
    log3 = InteliLogger.get_logger('log1')
    assert log1 is log3
    
    log1.debug('This is a debug message')
    log1.info('This is an info message')
    log1.warning('This is a warning message')
    log1.error('This is an error message')
    log1.critical('This is a critical message')

    log2.debug('This is a debug message')
    log2.info('This is an info message')    
    log2.warning('This is a warning message')
    log2.error('This is an error message')
    log2.critical('This is a critical message')

if __name__ == "__main__":
    test_inteli_logger()
