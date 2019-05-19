"""
    ExchangeWrapperRegistery is a class for keep track of concrete implementations of IExchangeWrapper.
    
    This class will add each class which inherited from IExchangeWrapper and used @register_exchange decorator.

"""
from crypto_summoner.exchange_wrappers.iexchange_wrapper import IExchangeWrapper
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('ExchangeWrapperRegistery')

class ExchangeWrapperRegistery():
    """
    ExchangeWrapperRegistery Class.

    ExchangeWrapperRegistery is a class for keep track of concrete implementations of IExchangeWrapper.
    This class will add each class which inherited from IExchangeWrapper and used @register_exchange decorator.
    
    ...

    Attributes:
        REGISTERED_IEXCHANGE_WRAPPER_CLASSES (list): List of classes which inherited from IExchangeWrapper and used @register_exchange decorator.
    
    Methods:       
        register_exchange(cls, register_cls): A decorator which register a class inherited from IExchangeWrapper to this class REGISTERED_IEXCHANGE_WRAPPER_CLASSES list. 
    """
    
    REGISTERED_IEXCHANGE_WRAPPER_CLASSES = []

    @classmethod
    def register_exchange(cls, register_cls):
        """
        Register a class inherited from IExchangeWrapper to this class REGISTERED_IEXCHANGE_WRAPPER_CLASSES list.     
        
        Args:        
            register_cls (IExchangeWrapper): The class reference which inherited from IExchangeWrapper. Provided by class decorator behaviour.
        """
        # TODO: Check if the register_cls isinstance of IExchangeWrapper.
        #       Right now it is only instance of abc.ABCMeta due to inheritance of IExchangeWrapper from ABC.
        #print(type(register_cls))
        #print(isinstance(register_cls, IExchangeWrapper))
        #assert isinstance(register_cls, IExchangeWrapper), "Decorated class is not inherited from IExchangeWrapper."
        cls.REGISTERED_IEXCHANGE_WRAPPER_CLASSES.append(register_cls)
        logger.debug(f"ExchangeWrapper class ({register_cls}) registered in ExchangeWrapperRegistery")
        return register_cls