"""
    GeneralExchangeFactory is a class inherited from IExchangeFactory for initializing IExchangeWrapper concrete implementations.
    
    Any Exchange SDK is wrapped in a class inheriting from IExchangeWrapper abstract class.
    
"""

import asyncio

from crypto_summoner.exchange_factory.iexchange_factory import IExchangeFactory
from crypto_summoner.exchange_wrappers.exchange_wrapper_registery import ExchangeWrapperRegistery
from crypto_summoner.config.config import Config
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('GeneralExchangeFactory')


class GeneralExchangeFactory(IExchangeFactory):
    """
    GeneralExchangeFactory Class

    ExchangeFactoryGeneral is a class inherited from IExchangeFactory for initializing IExchangeWrapper concrete implementations.
    Any Exchange SDK is wrapped in a class inheriting from IExchangeWrapper abstract class.
    Design Pattern: Abstract Factory

    ...

    Attributes:
        _registered_exchange_wrappers (dic): Dictionary of names and classes which inherited from IExchangeWrapper class 
            and registered.
        _initialized_exchange_wrappers (dic): Dictionary of names and classes which inherited from IExchangeWrapper class
            and initialized.
    
    Methods:       
        create_exchange(self, exchange_name, credential_dic): Creates a concrete object of the requested exchange wrapper. 
        register_exchange(self, exchange_name, exchange_wrapper_class_reference): Registers an IExchangeWrapper concrete implementation class. 
    """

    def __init__(self):
        """
        Inits IExchangeFactory.

        It initializes _registered_exchange_wrappers and _initialized_exchange_wrappers dictionaries.

        Attributes:
        _registered_exchange_wrappers (dic): Dictionary of names and classes which inherited from IExchangeWrapper class 
            and registered.
        _initialized_exchange_wrappers (dic): Dictionary of names and classes which inherited from IExchangeWrapper class
            and initialized.
        """

        IExchangeFactory.__init__(self)
        logger.info(f"Registered Exchange Wrappers Classes:\n{ExchangeWrapperRegistery.REGISTERED_IEXCHANGE_WRAPPER_CLASSES}")

    
    async def create_exchange(self, exchange_name, credential_dic):
        """
        Creates a concrete object of the requested exchange wrapper. 
        
        It is definde as async function because this code might be Network-bound.
        Using async will enable us to 'await' this function and not to block other tasks.
        
        Args:
            exchange_name (str): Name of the exchange we want to initialize.
            credential_dic (str): The exchange credentials dictionary.
        
        Returns:
            If successfull returns a IExchangeWrapper, otherwise None.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        exchange_class = self.registered_exchange_wrappers.get(exchange_name, None)
        if not exchange_class:
            logger.warning(f"No registered exchange wrapper by the name of {exchange_name}")
            return None
        try:
            self.initialized_exchange_wrappers[exchange_name] = exchange_class(credential_dic)
            logger.info(f"Initialization of ExchangeWrapper: {exchange_name} successful.")
            return self.initialized_exchange_wrappers[exchange_name]
        except Exception as e:
            logger.exception(f"Failed to initialize exchange wrapper by the name of {exchange_name}")
    
    def register_exchange(self, exchange_name, exchange_wrapper_class_reference):
        """
        Registers an IExchangeWrapper in this class _registered_exchange_wrappers dictionary.

        It registeres an IExchangeWrapper concrete implementation class by adding {'{exchange_name}':exchange_wrapper_class_reference}
        to initialized_exchange_wrappers dictionary.
        
        Args:
            exchange_name (str): Name of the exchange we want to initialize.
            exchange_wrapper_class_reference (IExchangeWrapper): IExchangeWrapper concrete implementation class reference.
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If exchange name is already registered with different class reference.
        """

        self.registered_exchange_wrappers[exchange_name] = exchange_wrapper_class_reference
        logger.info(f"Register ExchangeWrapper: {exchange_name} successful.")

    def register_all_exchanges(self):
        """
        Registers all IExchangeWrapper concrete implementations which is in ExchangeWrapperRegistery.

        It registeres all IExchangeWrapper concrete implementation class by calling register_exchange method.
              
        Returns:
            Returns nothing.  
        
        """

        for exchange in ExchangeWrapperRegistery.REGISTERED_IEXCHANGE_WRAPPER_CLASSES:            
            self.register_exchange(exchange.__name__, exchange)           
    
    async def create_all_exchanges(self):
        """
        Creates concrete objects of the all exchange wrappers. 
        
        It is definde as async function because this code might be Network-bound due to its usage of create_exchange method.
        Using async will enable us to 'await' this function and not to block other tasks.
        
        Args:
            
        
        Returns:
            
        
        Raises:
            
        """
        for exchange_name in self.registered_exchange_wrappers:
            # TODO change credentials to exchange_wrapper_initialization_config
            # get credentials by exchange_name from Config
            credentials = Config.get_property(exchange_name) 
            await self.create_exchange(exchange_name, credentials)

    
    @property
    def registered_exchange_wrappers(self):
        """
        GeneralExchangeFactory _registered_exchange_wrappers getter.
               
        Returns:
            Returns _registered_exchange_wrappers dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        return self._registered_exchange_wrappers
    
    @registered_exchange_wrappers.setter    
    def registered_exchange_wrappers(self, registered_exchange_wrappers_dic):
        """
        GeneralExchangeFactory _registered_exchange_wrappers setter.
        
        Args:
            registered_exchange_wrappers_dic (dic): Dictionary of names and classes which inherited from IExchangeWrapper class. 
            and used decorator to register in IExchangeFactory. e.g. {'Binance': BinanceExchangeWrapper}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        self._registered_exchange_wrappers = registered_exchange_wrappers_dic
    
    @property    
    def initialized_exchange_wrappers(self):
        """
        GeneralExchangeFactory _initialized_exchange_wrappers getter.
               
        Returns:
            Returns _initialized_exchange_wrappers dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        return self._initialized_exchange_wrappers
    
    @initialized_exchange_wrappers.setter
    def initialized_exchange_wrappers(self, initialized_exchange_wrappers_dic):
        """
        GeneralExchangeFactory _initialized_exchange_wrappers setter.
        
        Args:
            initialized_exchange_wrappers_dic (dic): Dictionary of names and classes which inherited from IExchangeWrapper class.
            and initialized using the create_exchange e.g. {'Binance': BinanceExchangeWrapper}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        self._initialized_exchange_wrappers = initialized_exchange_wrappers_dic
    
async def test_general_exchange_factory():
    from crypto_summoner.config.config import Config
    gef = GeneralExchangeFactory()    
    cred_dic = Config.get_property('BinanceExchangeWrapper')
    gef.register_all_exchanges()
    await gef.create_all_exchanges()
    #await gef.create_exchange('BinanceExchangeWrapper', cred_dic)
    #await gef.create_exchange('NoExchangeWrapper', cred_dic)
if __name__ == "__main__":
    asyncio.run(test_general_exchange_factory())