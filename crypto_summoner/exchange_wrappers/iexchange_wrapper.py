"""
    IExchangeWrapper is an abstract class for wrapping exchanges SDKs.
    
    This class will define the methods that each SDK wrapper class must implement.

"""

from abc import ABC, abstractmethod
import asyncio

from crypto_summoner.symbols_interface.symbols_interface import SymbolsInterface


class IExchangeWrapper(ABC):
    """
    IExchangeWrapper Class

    IExchangeWrapper is an abstract class for wrapping exchanges SDKs.
    This class will define the methods that each SDK wrapper class must implement.
    Design Pattern: Adapter

    ...

    Attributes:
        _credential (dic): Exchange credentials dictionary. e.g. {'API_KEY':'', 'API_SECRET': ''}
    
    Methods:       
        get_deposit_address(self, symbol): For a specified symbol, this function return the exchange deposit address.
        withdraw(self, symbol, from_addr, to_addr, amount): It send the exchange a request for withdrawal.
        get_price_by_symbol(self, symbol): It send the exchange a request for price of a the specified symbol.
        get_prices(self): It send the exchange a request for all of its symbol prices.        
    """
    
    def __init__(self, credential_dic):
        """
        Inits IExchangeWrapper with exchange credential dic.
        Call this init in derived __init__ functions. 
        class derived(IExchangeWrapper):
            def __init():
                IExchangeWrapper.__init__(self, credential_dic)
        
        Args:        
            credential_dic (str): The exchange credentials dictionary.
        """

        self._credential = credential_dic
        self._symobl_interface = SymbolsInterface

    @property
    @abstractmethod
    def credential(self):
        """
        IExchangeWrapper _credential getter.
               
        Returns:
            Returns _credential dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
        #raise NotImplementedError(f"{self.credential.__name__} is an abstract property. Override it in subclasses.")
    
    @credential.setter
    @abstractmethod
    def credential(self, credential_dic):
        """
        IExchangeWrapper _credential setter.
        
        Args:
            credential_dic (dic): Exchange credentials dictionary. e.g. {'API_KEY':'', 'API_SECRET': ''}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
        
        #raise NotImplementedError(f"{self.credential.__name__} is an abstract property. Override it in subclasses.")

    @property
    @abstractmethod
    def symobl_interface(self):
        """
        IExchangeWrapper _symobl_interface getter.
               
        Returns:
            Returns SymbolInterface.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """        

    @symobl_interface.setter
    @abstractmethod
    def symobl_interface(self, symobl_interface):
        """
        IExchangeWrapper _symobl_interface setter.
        
        Args:
            symobl_interface (SymbolInterface): a SymbolInterface
                concrete implementation.
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

    @abstractmethod
    async def get_deposit_address(self, symbol):
        """
        For a specified symbol, this function return the exchange deposit address.

        It is definde as async function because this code will be Network-bound. 
        Using async will enable us to 'await' this function and not to block our code.
        
        Args:
            symbol (str): Symbol which we want the deposit address. e.g. 'BTCETH'
        
        Returns:
            Returns the address string
        
        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If symbol is None or empty or not in !!!symbols_enum!!!
        """

        #raise NotImplementedError(f"{self.get_deposit_address.__name__} is an abstract method. Override it in subclasses.")
    
    @abstractmethod
    async def withdraw(self, symbol, from_addr, to_addr, amount):
        """
        It send the exchange a request for withdrawal.

        It is definde as async function because this code will be Network-bound. 
        Using async will enable us to 'await' this function and not to block our code.
        
        Args:
            symbol (str): Symbol which we want the deposit address. e.g. 'BTCETH'
            from_addr (str): The crypto address which we want to withdraw
            to_addr (str): The crypto destination address
            amount (float): The amount of the transaction
        
        Returns:
            Returns True if withdraw request sent successfully, False otherwise.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If symbol is None or empty or not in !!!symbols_enum!!!
            ValueError: If from_addr is None or empty or not valid
            ValueError: If to_addr is None or empty or not valid
            ValueError: If amount is None or empty or not valid
        """

        #raise NotImplementedError(f"{self.withdraw.__name__} is an abstract method. Override it in subclasses.")
    
    @abstractmethod
    async def get_price_by_symbol(self, symbol):
        """
        It send the exchange a request for price of a the specified symbol.
        
        It is definde as async function because this code will be Network-bound. 
        Using async will enable us to 'await' this function and not to block our code.

        Args:
            symbol (str): Symbol which we want the deposit address. e.g. 'BTCETH'
        
        Returns:
            Returns the symbol price
        
        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If symbol is None or empty or not in !!!symbols_enum!!!
        """
        
        #raise NotImplementedError(f"{self.get_price_by_symbol.__name__} is an abstract method. Override it in subclasses.")
    
    @abstractmethod
    async def get_prices(self):
        """
        It send the exchange a request for all of its symbol prices.

        It is definde as async function because this code will be Network-bound. 
        Using async will enable us to 'await' this function and not to block our code.
       
        Returns:
            Returns the prices dictionary
        
        Raises:
            NotImplementedError: This function must be override in derived classes           
        """

        #raise NotImplementedError(f"{self.get_prices.__name__} is an abstract method. Override it in subclasses.")


async def main():
    class TestIExchangeWrapper(IExchangeWrapper):
        def __init__(self, credential_dic):
            IExchangeWrapper.__init__(self, credential_dic)
    
        @property   
        def credential(self):
            return self._credential
        
        @credential.setter   
        def credential(self, credential_dic):
            self._credential = credential_dic
    
        async def get_deposit_address(self, symbol):
            pass
        
        async def withdraw(self, symbol, from_addr, to_addr, amount):
            pass       
            
        async def get_price_by_symbol(self, symbol=None):
            pass
            
        async def get_prices(self):
            pass


    exhan = TestIExchangeWrapper({'API_KEY':'123'})
    print(exhan.credential)
    exhan.credential = {'API_KEY':'changed'}
    print(exhan.credential)
    await exhan.get_deposit_address('456')
    exhan.register_exchange_handler()

if __name__ == "__main__":
    asyncio.run(main())