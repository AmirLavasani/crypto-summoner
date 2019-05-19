"""
    IExchangeFactory is an abstract class for initializing IExchangeWrapper concrete implementations.
    
    Any Exchange SDK is wrapped in a class inheriting from IExchangeWrapper abstract class.
    
"""

from abc import ABC, abstractmethod

class IExchangeFactory(ABC):
    """
    IExchangeFactory Class

    IExchangeFactory is an abstract class for initializing IExchangeWrapper concrete implementations.
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

        self._registered_exchange_wrappers = {}
        self._initialized_exchange_wrappers = {}
    
    @abstractmethod
    async def create_exchange(self, exchange_name, credential_dic):
        """
        Creates a concrete object of the requested exchange wrapper. 
        
        It is definde as async function because this code might be Network-bound.
        Using async will enable us to 'await' this function and not to block our code.
        
        Args:
            exchange_name (str): Name of the exchange we want to initialize.
            credential_dic (str): The exchange credentials dictionary.
        
        Returns:
            If successfull returns a IExchangeWrapper, otherwise None.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
    
    @abstractmethod
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

    @property
    @abstractmethod
    def registered_exchange_wrappers(self):
        """
        IExchangeFactory _registered_exchange_wrappers getter.
               
        Returns:
            Returns _registered_exchange_wrappers dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
    
    @registered_exchange_wrappers.setter
    @abstractmethod
    def registered_exchange_wrappers(self, registered_exchange_wrappers_dic):
        """
        IExchangeFactory _registered_exchange_wrappers setter.
        
        Args:
            registered_exchange_wrappers_dic (dic): Dictionary of names and classes which inherited from IExchangeWrapper class. 
            and used decorator to register in IExchangeFactory. e.g. {'Binance': BinanceExchangeWrapper}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
    
    @property
    @abstractmethod
    def initialized_exchange_wrappers(self):
        """
        IExchangeFactory _initialized_exchange_wrappers getter.
               
        Returns:
            Returns _initialized_exchange_wrappers dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
    
    @initialized_exchange_wrappers.setter
    @abstractmethod
    def initialized_exchange_wrappers(self, initialized_exchange_wrappers_dic):
        """
        IExchangeFactory _initialized_exchange_wrappers setter.
        
        Args:
            initialized_exchange_wrappers_dic (dic): Dictionary of names and classes which inherited from IExchangeWrapper class.
            and initialized using the create_exchange e.g. {'Binance': BinanceExchangeWrapper}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
