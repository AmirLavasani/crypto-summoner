"""
    ICryptoDataPreserver is an abstract class for
     preserving data gathered from a summoner.

    Any kind of preserver class for preserving data
     from a concrete implementation of a ISummoner should
     inherit from ICryptoDataPreserver.

"""

from abc import ABC, abstractmethod
import asyncio

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('ICryptoDataPreserver')


class ICryptoDataPreserver(ABC):
    """
    ICryptoDataPreserver is an abstract class for
     preserving data gathered from a summoner.

    Any kind of preserver class for preserving data
     from a concrete implementation of a ISummoner should
     inherit from ICryptoDataPreserver.

    Design Pattern: Bridge (kind of)

    ...

    Attributes:

    Methods:
        async on_data(self, data): called from ICryptoDataProxy when
         new data is available.

    """

    def __init__(self, preserver_configuration):
        """
        Inits ICryptoDataPreserver.

        Call this init in derived __init__ functions.
        class derived(ICryptoDataPreserver):
            def __init():
                ICryptoDataPreserver.__init__(self, preserver_configuration)

        Attributes:
            preserver_configuration (dic): a dictionary
             for the preserver configurations.

        """
        self.preserver_configuration = preserver_configuration

    @property
    @abstractmethod
    def preserver_configuration(self):
        """
        ICryptoDataSummoner _preserver_configuration getter.

        Returns:
            Returns _preserver_configuration dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @preserver_configuration.setter
    @abstractmethod
    def preserver_configuration(self, preserver_configuration):
        """
        ICryptoDataSummoner _preserver_configuration setter.

        Args:
        preserver_configuration (dic): a dictionary
             for the summoner execution configuration.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @abstractmethod
    async def on_data(self, data):
        """
        ICryptoDataPreserver on_data method.
        
        This method is called from ICryptoDataProxy when
         new data is available.

        """


async def main():
    import asyncio
    from aiofile import AIOFile, Reader, Writer

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
            async with AIOFile(self.preserver_configuration['fileName'], 'w+') as afp:
                writer = Writer(afp)
                writer.write(f'{data}\n')
    
    cdp = TestICryptoDataPreserver({'fileName': '/tmp/crypto_data'})
    logger.info(cdp)


if __name__ == "__main__":
    asyncio.run(main())
