"""
    An Enum Class for homogenizing the diffrenet
     representation of binance exchange market symbols.
"""

from enum import unique
from crypto_summoner.symbols_interface.symbols_enum import SymbolsEnum


@unique
class ExmoSymbolsEnum(SymbolsEnum):
    """
    ExmoSymbolsEnum Class

    ExmoSymbolsEnum is an Enum Class for homogenizing the diffrenet
     representation of binance exchange market symbols.

    ...

    It inherits SymbolsEnum class.
    Each SymbolInterface should have a valid concrete SymbolsEnums
     for the exchange symbols representation.

    """

    BTCUSDT = "BTC_USDT"
    ETHUSDT = "ETH_USDT"
    LTCUSDT = "LTC_USDT"
    XRPUSDT = "XRP_USDT"
    EOSUSDT = "EOS_USDT"
    BCHABCUSDT = "BCHABC_USDT"
    BCHSVUSDT = "BCHSV_USDT"
    XLMUSDT = "XLM_USDT"
    BCHUSDT = "BCH_USDT"
    TRXUSDT = "TRX_USDT"
    BSVUSDT = "BSV_USDT"
    DASHUSDT = "DASH_USDT"
    NEOUSDT = "NEO_USDT"
    USDCUSDT = "USDC_USDT"
    ETHBTC = "ETH_BTC"
    LTCBTC = "LTC_BTC"
    NEOBTC = "NEO_BTC"
    ZECBTC = "ZEC_BTC"
    BCHBTC = "BCH_BTC"
    EOSBTC = "EOS_BTC"
    XLMBTC = "XLM_BTC"
    LTCETH = "LTC_ETH"
    ZECETH = "ZEC_ETH"
    EOSETH = "EOS_ETH"
    XLMETH = "XLM_ETH"


def test_binance_symbols_enum():
    print(ExmoSymbolsEnum.ETHBTC.value)
    print(ExmoSymbolsEnum.validate())


if __name__ == "__main__":
    test_binance_symbols_enum()
