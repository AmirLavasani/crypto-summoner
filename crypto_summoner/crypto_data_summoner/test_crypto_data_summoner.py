import random
import asyncio

from crypto_summoner.crypto_data_summoner.icrypto_data_summoner import ICryptoDataSummoner


class TestICryptoDataSummoner(ICryptoDataSummoner):
    def __init__(self, initialized_exchange_wrappers, summoner_configuration):
        ICryptoDataSummoner.__init__(self, initialized_exchange_wrappers, summoner_configuration)

    @property
    def summoner_configuration(self):
        return self._summoner_configuration

    @summoner_configuration.setter
    def summoner_configuration(self, summoner_configuration):
        if "intervals" not in summoner_configuration:
            raise ValueError(f"summoner_configuration is not valid for {__class__.__name__}")
        self._summoner_configuration = summoner_configuration

    async def summon(self):
        while True:
            await asyncio.sleep(self.summoner_configuration['intervals'])
            yield random.randint(1, 100)
