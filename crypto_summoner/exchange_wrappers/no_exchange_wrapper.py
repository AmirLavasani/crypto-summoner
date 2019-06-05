"""
    NoExchangeWrapper is the class responsible for wrapping noexchange exchange SDKs.
    
    This class inherits from IExchangeWrapper abstract class.

"""

import asyncio
from crypto_summoner.exchange_wrappers.iexchange_wrapper import IExchangeWrapper
from crypto_summoner.exchange_wrappers.exchange_wrapper_registery import ExchangeWrapperRegistery
from crypto_summoner.symbols_interface.noexchange_symbols import NoexchangeSymbols


@ExchangeWrapperRegistery.register_exchange
class NoExchangeWrapper(IExchangeWrapper):
    """
    NoExchangeWrapper Class

    NoExchangeWrapper is the class responsible for wrapping noexhchange exchange SDK.
    This class inherits from IExchangeWrapper abstract class.
    Design Pattern: Adapter

    ...

    Attributes:
        _credential (dic): Exchange credentials dictionary. e.g. {'API_KEY':'', 'API_SECRET': ''}
        _symobl_interface (SymbolInterface): a SymbolInterface
            concrete implementation.

    Methods:       
        get_deposit_address(self, symbol): For a specified symbol, this function return the exchange deposit address.
        withdraw(self, symbol, from_addr, to_addr, amount): It send the exchange a request for withdrawal.
        get_price_by_symbol(self, symbol): It send the exchange a request for price of a the specified symbol.
        get_prices(self): It send the exchange a request for all of its symbol prices.        
    """
    
    def __init__(self, credential_dic):
        """
        Inits NoExchangeWrapper with exchange credential dic.
                
        Args:        
            credential (str): The exchange credentials dictionary.
        
        Raises:
            ValueError: If credential_dic does not include 'API_KEY' and 'API_SECRET'
        """

        IExchangeWrapper.__init__(self, credential_dic)
        
    @property
    def client(self):
        """
        NoExchangeWrapper _client getter.

        Returns:
            Returns _client Client object.
        """

        return self._client

    @client.setter
    def client(self, client_object):
        """
        NoExchangeWrapper _client setter.
        
        Args:
            client_object (Client): A noexhange.client Client object.
        
        Returns:
            Returns nothing.  
        
        Raises:
            ValueError: If client_object is not an instance 
                of noexchange.client Client object.
        """

        self._client = client_object

    @property
    def credential(self):
        """
        IExchangeWrapper _credential getter.
               
        Returns:
            Returns _credential dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """

        return self._credential
    
    @credential.setter
    def credential(self, credential_dic):
        """
        IExchangeWrapper _credential setter.
        
        Args:
            credential_dic (dic): Exchange credentials dictionary. e.g. {'API_KEY':'', 'API_SECRET': ''}
        
        Returns:
            Returns nothing.  
        
        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If credential_dic is not a dictionary
        """

        if not isinstance(credential_dic,dict):
            raise ValueError("Function argument credential_dic should be a dictionary.")
        self._credential = credential_dic
    @property
    def symobl_interface(self):
        """
        IExchangeWrapper _symobl_interface getter.
               
        Returns:
            Returns SymbolInterface.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        
        """

        return self._symobl_interface

    @symobl_interface.setter
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
            ValueError: if symbol_interface not validated.
            ValueError: if symbol_interface not an instance of NoexchangeSymbols.
        """

        if not isinstance(symobl_interface, type(NoexchangeSymbols)):
            raise ValueError("symbol_interface is not subclass of NoexchangeSymbols")
        if not symbols_interface.is_valid():
            raise ValueError("symbol_interface is not valid implementation of NoexchangeSymbols ")

        self._symobl_interface = symobl_interface

    def validate_symbols_inteface(symbol_interface):
        """
        Validates a concrete implementation of SymbolInterface
        
        Validates a concrete implementation of and also 
            validates that this SymbolInterface is instance 
            of NoexchangeSymbols.

        Args:
            symobl_interface (SymbolInterface): a SymbolInterface
                concrete implementation.
        
        Returns:
            Returns nothing.  
        
        Raises:
            ValueError: if symbol_interface not validated.
            ValueError: if symbol_interface not an instance of NoexchangeSymbols.
        """

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

        pass
        
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

        pass
        
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
        
        pass
    
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

        return self.client.get_all_tickers()


async def main():  
    api_key = "no_api_key"
    api_secret = "no_api_secret"
    cred_dic = {'API_KEY': api_key, 'API_SECRET': api_secret}
    new = NoExchangeWrapper(cred_dic)    

if __name__ == "__main__":
    asyncio.run(main())