"""
    An abstract Enum Class for homogenizing the diffrenet
    representation of market symbols in exchanges.
"""

from abc import ABC, abstractmethod


class SymbolsInterface(ABC):
    """
    SymbolsInterface Class

    SymbolsInterface is an abstract Class for exchange wrappers
    to access their SymbolEnum.

    ...

    It inherits from ABC abstrac class.
    Each exchange should have a concrete implementation
    of SymbolsInterface for the exchange symbols representation.

    Attributes:
        _symbols_enum (SymbolsEnum): class reference to the
            exchange SymbolsEnum concrete implementation.

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

    _symbols_enum = None
    _symbols_enum_invert_dictionary = None
    # {v: k for k, v in SymbolsEnum.__members__.items()}

    @classmethod
    @abstractmethod
    def get_symbols_enum(cls):
        """
        SymbolsInterface _symbols_enum getter.

        Returns:
            Returns _symbols_enum SymbolsInterface object.
        """

    @classmethod
    @abstractmethod
    def get_symbols_enum_invert_dictionary(cls):
        """
        SymbolsInterface _symbols_enum_invert_dictionary getter.

        Returns:
            Returns _symbols_enum_invert_dictionary dictionary.
        """

    @classmethod
    @abstractmethod
    def is_valid(cls):
        """
        This method checks if _symbols_enum is valid.

        Returns:
            Returns True if valid, False otherwise.
        """

    @classmethod
    @abstractmethod
    def get_exchange_symbol_by_standard_name(cls, standard_symbol_name):
        """
        This method returns the exchange representation of a symbol.

        Args:
            standard_symbol_name (str): standard symbol name.

        Returns:
            Returns standard symbol name (str) if it exist
            in cls.symbols_enum, None otherwise.
        """

    @classmethod
    @abstractmethod
    def get_standard_symbol_by_exchange_name(cls, exchange_symbol_name):
        """
        This method returns the standard representation of a symbol.

        Args:
            exchange_symbol_name (str): exchange symbol name.

        Returns:
            Returns standard symbol name (str) if it exist
            in cls.symbols_enum, None otherwise.
        """
