import asyncio
from aiofile import AIOFile, Reader, Writer

from crypto_summoner.crypto_data_preserver.icrypto_data_preserver import ICryptoDataPreserver

class TestICryptoDataPreserver(ICryptoDataPreserver):
    def __init__(self, preserver_configuration):
        ICryptoDataPreserver.__init__(self, preserver_configuration)

    @property
    def preserver_configuration(self):
        return self._preserver_configuration

    @preserver_configuration.setter
    def preserver_configuration(self, preserver_configuration):
        if "fileName" not in preserver_configuration:
            raise ValueError(f"preserver_configuration is not valid for {__class__.__name__}")
        self._preserver_configuration = preserver_configuration

    async def on_data(self, data):
        async with AIOFile(self.preserver_configuration['fileName'], 'a+') as afp:
            writer = Writer(afp)
            await writer(f'{data}\n')
