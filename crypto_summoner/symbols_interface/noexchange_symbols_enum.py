"""
    An Enum Class for homogenizing the diffrenet
     representation of noexchange market symbols.
"""

from enum import unique
from crypto_summoner.symbols_interface.symbols_enum import SymbolsEnum


@unique
class NoExchangeSymbolsEnum(SymbolsEnum):
    """
    NoExchangeSymbolsEnum Class

    NoExchangeSymbolsEnum is an Enum Class for homogenizing the diffrenet
     representation of binance exchange market symbols.

    ...

    It inherits SymbolsEnum class.
    Each SymbolInterface should have a valid concrete SymbolsEnums
     for the exchange symbols representation.

    """

    BTCUSDT = "BTCUSDT"
    ETHUSDT = "ETHUSDT"
    LTCUSDT = "LTCUSDT"
    XRPUSDT = "XRPUSDT"
    EOSUSDT = "EOSUSDT"
    BCHABCUSDT = "BCHABCUSDT"
    BCHSVUSDT = "BCHSVUSDT"
    XLMUSDT = "XLMUSDT"
    BCHUSDT = "BCHUSDT"
    TRXUSDT = "TRXUSDT"
    BSVUSDT = "BSVUSDT"
    DASHUSDT = "DASHUSDT"
    NEOUSDT = "NEOUSDT"
    USDCUSDT = "USDCUSDT"
    ETHBTC = "ETHBTC"
    LTCBTC = "LTCBTC"
    NEOBTC = "NEOBTC"
    ZECBTC = "ZECBTC"
    BCHBTC = "BCHBTC"
    EOSBTC = "EOSBTC"
    XLMBTC = "XLMBTC"
    LTCETH = "LTCETH"
    ZECETH = "ZECETH"
    EOSETH = "EOSETH"
    XLMETH = "XLMETH"

def test_noexchange_symbols_enum():
    print(NoExchangeSymbolsEnum.ETHBTC.value)
    print(NoExchangeSymbolsEnum.validate())


if __name__ == "__main__":
    test_noexchange_symbols_enum()
