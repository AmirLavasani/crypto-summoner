"""
    An concret implementation of SymbolsInterface abstract enum class.
    representation of binance exchanges market symbols.
"""

from crypto_summoner.symbols_interface.symbols_interface import SymbolsInterface
from crypto_summoner.symbols_interface.binance_symbols_enum import BinanceSymbolsEnum
from crypto_summoner.symbols_interface.symbols_enum import SymbolsEnum


class BinanceSymbols(SymbolsInterface):
    """
    BinanceSymbols Class

    BinanceSymbols is an concrete implementation of
    SymbolsInterface class.

    It will for provide BinanceExchangeWrapper
    access BinanceSymbolsEnum
    ...

    It inherits from SymbolsInterface abstrac class.

    Attributes:
        _symbols_enum (SymbolsEnum): class reference to the
            BinanceSymbolsEnum.
        _symbols_enum_revere_dictionary (dic): reverse dictionary
            of _symbols_enum

    Methods:
        get_symbols_enum(cls): This class method is
            SymbolsInterface _symbols_enum getter.
        get_symbols_enum_invert_dictionary(cls): This class method is
            SymbolsInterface _symbols_enum_invert_dictionary getter.
        is_valid(cls): This method checks if _symbols_enum is valid.
        get_exchange_symbol_by_standard_name(cls, standard_symbol_name):
            This method returns the exchange representation of a symbol.
        get_standard_symbol_by_exchange_name(cls, exchange_symbol_name):
            This method returns the standard representation of a symbol.

    """

    _symbols_enum = BinanceSymbolsEnum
    _symbols_enum_invert_dictionary = {v.value: k for k, v in BinanceSymbolsEnum.__members__.items()}

    @classmethod
    def get_symbols_enum(cls):
        """
        SymbolsInterface _symbols_enum getter.

        Returns:
            Returns _symbols_enum SymbolsInterface object.
        """

        return cls._symbols_enum

    @classmethod
    def get_symbols_enum_invert_dictionary(cls):
        """
        SymbolsInterface _symbols_enum_invert_dictionary getter.

        Returns:
            Returns _symbols_enum_invert_dictionary dictionary.
        """

        return cls._symbols_enum_invert_dictionary

    @classmethod
    def is_valid(cls):
        """
        This method checks if _symbols_enum is valid.

        Returns:
            Returns True if valid, False otherwise.

        Raises:
            TypeError: if _symbols_enum is not inherited from SymbolsEnum
        """

        if isinstance(cls._symbols_enum, type(SymbolsEnum)):
            return cls._symbols_enum.validate()

        raise TypeError("_symbols_enum is not inherited from SymbolsEnum.")

    @classmethod
    def get_exchange_symbol_by_standard_name(cls, standard_symbol_name):
        """
        This method returns the exchange representation of a symbol.

        Args:
            standard_symbol_name (str): standard symbol name.

        Returns:
            Returns standard symbol name (str) if it exist
            in cls.symbols_enum, None otherwise.
        """

        symbol_enum = cls.get_symbols_enum().__members__.get(standard_symbol_name, None)
        if not symbol_enum:
            return None
        return symbol_enum.value

    @classmethod
    def get_standard_symbol_by_exchange_name(cls, exchange_symbol_name):
        """
        This method returns the standard representation of a symbol.

        Args:
            exchange_symbol_name (str): exchange symbol name.

        Returns:
            Returns standard symbol name (str) if it exist
            in cls.symbols_enum, None otherwise.
        """

        return cls.get_symbols_enum_invert_dictionary().get(exchange_symbol_name, None)


def test_binance_symbols():
    print(BinanceSymbols.is_valid())
    s = BinanceSymbols.get_symbols_enum()
    for enum in list(s):
        print(enum.value)
    print(BinanceSymbols.get_exchange_symbol_by_standard_name('ETHBTC'))
    print(BinanceSymbols.get_standard_symbol_by_exchange_name('ETHBTC'))


if __name__ == "__main__":
    test_binance_symbols()
