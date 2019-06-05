"""
    An Enum Class for homogenizing the diffrenet
    representation of market symbols in exchanges.
"""

from enum import Enum, unique, EnumMeta

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('SymbolsEnum')


@unique
class SymbolsEnum(Enum):
    """
    SymbolsEnum Class

    SymbolsEnum is an Enum Class for homogenizing the diffrenet
    representation of market symbols in exchanges.

    ...

    It inherits Enum class.
    Each SymbolsInterface should have a valid concrete SymbolsEnums
    for the exchange symbols representation.

    Methods:
        validate(cls): This method validates the concrete SymbolsEnum of
            each exchange implementation.

    """

    @classmethod
    def validate(cls):
        """
        This method validates the concrete SymbolsEnum of
        each exchange implementation.

        Returns:
            Returns True if validated, False otherwise.

        """

        # TODO: Retrieve required symbols list from
        #       a yaml configuration file.
        logger.debug(f"validating {cls} Enum class.")
        symbols_list = [
            'ETHBTC',
            'LTCBTC',
            'BNBBTC',
            'NEOBTC',
            'BCCBTC'
        ]

        if not isinstance(cls, type(SymbolsEnum)):
            logger.debug(f"{cls} is not an instance of Enum class.")
            return False

        # go over all the Enum names which must be present
        # in the classes inherited from SymbolsEnum.
        for key in symbols_list:
            if not cls.__members__.get(key, None):
                logger.debug(f"{key} is not defined in inherited class {cls}.")
                return False

        return True


def test_symbols_enum_validation():
    
    @unique
    class TestSymbols(SymbolsEnum):
        ETHBTC = 'ETHBTC'
        LTCBTC = 'LTCBTC'
        BNBBTC = 'BNBBTC'
        NEOBTC = 'NEOBTC'
        BCCBTC = 'BCCBTC'
    print(BinanceSymbolsEnum.validate())


if __name__ == "__main__":
    test_symbols_enum_validation()
