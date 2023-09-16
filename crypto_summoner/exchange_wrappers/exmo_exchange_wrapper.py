"""
    ExmoExchangeWrapper is the class responsible for wrapping exmo exchange SDKs.

    This class inherits from IExchangeWrapper abstract class.

"""

import asyncio
import requests

from crypto_summoner.exchange_wrappers.iexchange_wrapper import IExchangeWrapper
from crypto_summoner.exchange_wrappers.exchange_wrapper_registery import ExchangeWrapperRegistery
from crypto_summoner.symbols_interface.exmo_symbols import ExmoSymbols


@ExchangeWrapperRegistery.register_exchange
class ExmoExchangeWrapper(IExchangeWrapper):
    """
    ExmoExchangeWrapper Class

    ExmoExchangeWrapper is the class responsible for wrapping exmo exchange SDK.
    This class inherits from IExchangeWrapper abstract class.
    Design Pattern: Adapter

    ...

    Attributes:
        _credential_dic (dic): Exchange credentials dictionary.
         e.g. {'API_KEY':'', 'API_SECRET': ''}. Right now are using
         public api so we dont need authentication.

        _symobl_interface (SymbolInterface): a SymbolInterface
         concrete implementation.

    Methods:
        get_deposit_address(self, symbol): For a specified symbol,
         this function return the exchange deposit address.

        withdraw(self, symbol, from_addr, to_addr, amount): It send
         the exchange a request for withdrawal.

        get_price_by_symbol(self, symbol): It send the exchange a
         request for price of a the specified symbol.

        get_prices(self): It send the exchange a request for all of
         its symbol prices.

    """

    def __init__(self, credential_dic):
        """
        Inits ExmoExchangeWrapper with exchange credential dic.

        Args:
            credential (str): The exchange credentials dictionary.

        Raises:
            ValueError: if ExmoSymbols not validated.

        """

        IExchangeWrapper.__init__(self, credential_dic)

        # TODO change client to a sdk client for this exhange
        # Right now we are using public API.

        self.client = None
        self._symobl_interface = ExmoSymbols

    @property
    def client(self):
        """
        ExmoExchangeWrapper _client getter.

        Returns:
            Returns _client Client object.
        """

        return self._client

    @client.setter
    def client(self, client_object):
        """
        ExmoExchangeWrapper _client setter.

        Args:
            client_object (Client): A exmo.client Client object.
             Right now are using public api so we dont use a SDK
             client for exmo exchange.

        Returns:
            Returns nothing.

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
            credential_dic (dic): Exchange credentials dictionary.
             e.g. {'API_KEY':'', 'API_SECRET': ''}. Right now are using
             public api so we dont need authentication.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be override in derived classes
            ValueError: If credential_dic is not a dictionary

        """

        if not isinstance(credential_dic, dict):
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
            ValueError: if symbol_interface not an instance of ExmoSymbols.
        """

        if not isinstance(symobl_interface, type(ExmoSymbols)):
            raise ValueError("symbol_interface is not subclass of ExmoSymbols")
        if not symobl_interface.is_valid():
            raise ValueError("symbol_interface is not valid implementation of ExmoSymbols ")

        self._symobl_interface = symobl_interface

    def validate_symbols_inteface(symbol_interface):
        """
        Validates a concrete implementation of SymbolInterface

        Validates a concrete implementation of and also
            validates that this SymbolInterface is instance
            of ExmoSymbols.

        Args:
            symobl_interface (SymbolInterface): a SymbolInterface
                concrete implementation.

        Returns:
            Returns nothing.

        Raises:
            ValueError: if symbol_interface not validated.
            ValueError: if symbol_interface not an instance of ExmoSymbols.

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
            ValueError: If symbol is None or empty or not in ExmoSymbols

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
            ValueError: If symbol is None or empty or not in ExmoSymbols
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
            ValueError: If symbol is None or empty or not in ExmoSymbols

        """

        return self.client.get_order_book(symbol=symbol)

    async def get_prices(self):
        """
        It send the exchange a request for all of its symbol prices.

        It is definde as async function because this code will be Network-bound.
        Using async will enable us to 'await' this function and not to block our code.

        Returns:
            Returns the prices dictionary

        Raises:
            NotImplementedError: This function must be override in derived classes.

        """
        resp = requests.get('https://api.exmo.com/v1/ticker/')
        prices = resp.json()

        symbols = self.symobl_interface.get_symbols_enum_invert_dictionary()

        filtered_prices = []
        for exchange_symbol in prices.keys():
            if exchange_symbol in symbols.keys():
                pair_price = float(prices.get(exchange_symbol)['last_trade'])
                symbol = self.symobl_interface.get_standard_symbol_by_exchange_name(exchange_symbol)
                {'symbol': 'ETHBTC', 'price': '0.00486530'}
                filtered_prices.append(
                    {
                        'symbol': symbol,
                        'price': str(pair_price)
                    }
                )
        return filtered_prices


async def main():
    from crypto_summoner.config.config import Config
    from crypto_summoner.exchange_factory.general_exchange_factory import GeneralExchangeFactory

    gef = GeneralExchangeFactory()

    cred_dic = Config.get_property("ExmoExchangeWrapper")
    gef.register_exchange("ExmoExchangeWrapper", ExmoExchangeWrapper)
    await gef.create_exchange("ExmoExchangeWrapper", cred_dic)
    beh = gef.get_exchange_wrapper("ExmoExchangeWrapper")
    prices = await beh.get_prices()
    print(prices)
    ethbtc = beh.symobl_interface.get_exchange_symbol_by_standard_name("ETHBTC")
    order_ethbtc = await beh.get_price_by_symbol(ethbtc)
    print(order_ethbtc)


if __name__ == "__main__":
    asyncio.run(main())
