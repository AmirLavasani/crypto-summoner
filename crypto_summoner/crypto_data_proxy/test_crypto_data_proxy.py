import asyncio

from crypto_summoner.crypto_data_proxy.icrypto_data_proxy import ICryptoDataProxy
from crypto_summoner.crypto_data_summoner.test_crypto_data_summoner import TestICryptoDataSummoner
from crypto_summoner.crypto_data_preserver.test_crypto_data_preserver import TestICryptoDataPreserver
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('TestICryptoDataProxy')


class TestICryptoDataProxy(ICryptoDataProxy):
    def __init__(self, crypto_data_summoner, crypto_data_preserver):
        ICryptoDataProxy.__init__(self, crypto_data_summoner, crypto_data_preserver)

    async def connect(self):
        async for data in self.crypto_data_summoner.summon():
            await self.crypto_data_preserver.on_data(data)

async def main():
    tis = TestICryptoDataSummoner({'exchangeWrappers': {}}, {'intervals': 5})
    logger.info(tis)

    cdp = TestICryptoDataPreserver({'fileName': '/tmp/crypto_data'})
    logger.info(cdp)

    #logger.info()
    proxy = TestICryptoDataProxy(tis, cdp)
    #proxy.bind()
    await proxy.connect()

if __name__ == "__main__":
    asyncio.run(main())