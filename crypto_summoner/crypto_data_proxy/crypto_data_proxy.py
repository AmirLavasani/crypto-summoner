"""
    CryptoDataProxy is a concrete implemetation of ICryptoDataSummoner
     bridging different crypto data summoners to different crypto 
     data preservers.

"""

import asyncio

from crypto_summoner.crypto_data_proxy.icrypto_data_proxy import ICryptoDataProxy
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('CryptoDataProxy')


class CryptoDataProxy(ICryptoDataProxy):
    """
    CryptoDataProxy is a concrete implemetation of ICryptoDataSummoner
     bridging different crypto data summoners to different crypto 
     data preservers.

    Any kind of proxy class for bridging an ICryptoDataSummoner
     concrete implementation and a ICryptoDataPreserver concrete
     implementation should inherit from ICryptoDataProxy.

    Design Pattern: Bridge (kind of)

    ...

    Attributes:
        _crypto_data_summoner (ICryptoDataSummoner): a concrete
         implementation of ICryptoDataSummoner abstract class.

        _crypto_data_preserver (ICryptoDataPreserver): a concrete
         implementation of ICryptoDataPreserver abstract class.

    Methods:
        bind(self): bind _crypto_data_summoner to _crypto_data_preserver

        unbind(self): unbind _crypto_data_summoner from _crypto_data_preserver

        async connect(self): This method will bind and connect _crypto_data_summoner
         to _crypto_data_preserver and pass through data from summoner
         to be preserver.

    """

    def __init__(self, crypto_data_summoner, crypto_data_preserver):
        """
        Inits CryptoDataProxy with _crypto_data_summoner
         and _crypto_data_preserver.
        
        According to ICryptoDataProxy we should call super init in
         derived __init__ functions.

        class derived(ICryptoDataProxy):
            def __init(self):
                ICryptoDataProxy.__init__(self,
                                    crypto_data_summoner,
                                    crypto_data_preserver
                                )
        Attributes:
            _crypto_data_summoner (ICryptoDataSummoner): a concrete
             implementation of ICryptoDataSummoner abstract class.

            _crypto_data_preserver (ICryptoDataPreserver): a concrete
             implementation of ICryptoDataPreserver abstract class.

            _bind (boolean): let data pass through proxy if True.

        """

        ICryptoDataProxy.__init__(self, crypto_data_summoner, crypto_data_preserver)

    async def connect(self):
        """
        CryptoDataProxy connect method.

        This method will bind and connect _crypto_data_summoner to
         _crypto_data_preserver and pass through data from summoner
          to be preserver.
        """

        async for data in self.crypto_data_summoner.summon():
            await self.crypto_data_preserver.on_data(data)
            logger.debug("Summoned data proxied to preserver.")


async def main():
    from crypto_summoner.exchange_factory.general_exchange_factory import GeneralExchangeFactory
    from crypto_summoner.crypto_data_summoner.general_crypto_data_summoner import GeneralCryptoDataSummoner
    from crypto_summoner.crypto_data_preserver.influx_crypto_data_preserver import InfluxCryptoDataPreserver

    gef = GeneralExchangeFactory()
    gef.register_all_exchanges()
    await gef.create_all_exchanges()

    gcds = GeneralCryptoDataSummoner(gef.initialized_exchange_wrappers, {'intervals': 30})
    icdp = InfluxCryptoDataPreserver({})

    proxy = CryptoDataProxy(gcds, icdp)
    proxy.bind()
    await proxy.connect()


if __name__ == "__main__":
    asyncio.run(main())
