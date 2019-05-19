"""
    BinanceExchangeHandler is the class responsible for wrapping binance exchange SDKs.
    
    This class inherits from ExchangeHandler abstract class.

"""

import asyncio
from exchange_handler import ExchangeHandler
from binance.client import Client


class BinanceExchangeHandler(ExchangeHandler):
    """
    BinanceExchangeHandler Class

    BinanceExchangeHandler is the class responsible for wrapping binance exchange SDK.
    This class inherits from ExchangeHandler abstract class.
    Design Pattern: Facade

    ...

    Attributes:
        _credential (dic): Exchange credentials dictionary. e.g. {'API_KEY':'', 'API_SECRET': ''}
    
    Methods:       
        get_deposit_address(self, symbol): For a specified symbol, this function return the exchange deposit address.
        withdraw(self, symbol, from_addr, to_addr, amount): It send the exchange a request for withdrawal.
        get_price_by_symbol(self, symbol): It send the exchange a request for price of a the specified symbol.
        get_prices(self): It send the exchange a request for all of its symbol prices.
        register_exchange_handler(): It register this class in a !!!exchanges object!!!
    """
    
    def __init__(self, credential_dic):
        """
        Inits BinanceExchangeHandler with exchange credential dic.
                
        Args:        
            credential (str): The exchange credentials dictionary.
        
        Raises:
            ValueError: If credential_dic does not include 'API_KEY' and 'API_SECRET'
        """
        ExchangeHandler.__init__(self, credential_dic)

        if not credential_dic.get('API_KEY', None) or not credential_dic.get('API_SECRET', None):
            raise ValueError("credential_dic is not in binance credential dictionary format. missing key API_KEY or API_SECRET")
        self.client = Client(credential_dic.get('API_KEY'), credential_dic.get('API_SECRET'))

    @property
    def client(self):
        """
        BinanceExchangeHandler _client getter.

        Returns:
            Returns _client Client object.
        """

        return self._client

    @client.setter
    def client(self, client_object):
        """
        BinanceExchangeHandler _client setter.
        
        Args:
            client_object (Client): A binance.client Client object.
        
        Returns:
            Returns nothing.  
        
        Raises:
            ValueError: If client_object is not an instance of binance.client Client object.
        """
        if not isinstance(client_object, Client):
            raise ValueError("Function argument client should be a valid binance.client Client object.")
        self._client = client_object

    @property
    def credential(self):
        """
        ExchangeHandler _credential getter.
               
        Returns:
            Returns _credential dictionary.
        
        Raises:
            NotImplementedError: This function must be override in derived classes
        """
        return self._credential
    
    @credential.setter
    def credential(self, credential_dic):
        """
        ExchangeHandler _credential setter.
        
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

    def register_exchange_handler():
        """
        It register this class in a !!!exchanges object!!!.
       
        Returns:
        
        Raises:
            NotImplementedError: This function must be override in derived classes           
        """

        pass

async def main():  
    api_key = "GUDngb2z8aUqkrzIXevAfD5WKlXe3BUgU3lo7FH42btd7uDpYeP5k0I295KU8JPB"
    api_secret = "ESrDPnoicw8rfJurgaCXHoGoHLUaL5S0RtxeG3Yvl05ZRjmZhiJSjgGTZ1z4BHtA"
    cred_dic = {'API_KEY': api_key, 'API_SECRET': api_secret}
    beh = BinanceExchangeHandler(cred_dic)
    prices = await beh.get_prices()
    print(prices)

if __name__ == "__main__":
    asyncio.run(main())