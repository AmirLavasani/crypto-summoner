"""
    ICryptoDataSummoner is an abstract class for retrieving
     exchange data from different IExchangeWrapper
     concrete implementations.

    Any kind of data request for retrieving data from
     IExchangeWrapper implementations concrete should
     inherit from ICryptoDataSummoner.

"""

from abc import ABC, abstractmethod
import asyncio

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('ICryptoDataSummoner')


class ICryptoDataSummoner(ABC):
    """
    ICryptoDataSummoner Class

    ICryptoDataSummoner is an abstract class for initializing
     ICryptoDataSummoner concrete implementations.

    Any kind of data request for retrieving data from
     IExchangeWrapper implementations concrete should
     inherit from ICryptoDataSummoner.

    Design Pattern: Bridge (kind of)

    ...

    Attributes:
        initialized_exchange_wrappers (dic):
         The initialized dictionary of
         exhcange wrappers. Using this dictionary
         the concrete implementation of ICryptoDataSummoner
         will request for data from different exchanges.

        summoner_configuration (dic): a dictionary
         for the summoner execution configuration.

    Methods:
        summon(self, initialized_exchange_wrappers, summoner_configuration):
         This method will execute the concrete implementation of ICryptoDataSummoner
         and request data from initialized exchange wrappers.
         

    """

    def __init__(self, initialized_exchange_wrappers, summoner_configuration):
        """
        Inits ICryptoDataSummoner with initialized_exchange_wrappers
         and summoner_configuration.

        Call this init in derived __init__ functions.
        class derived(ICryptoDataSummoner):
            def __init():
                ICryptoDataSummoner.__init__(self,
                                    initialized_exchange_wrappers,
                                    summoner_configuration
                                )
        Attributes:
            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ICryptoDataSummoner
             will request for data from different exchanges.

            summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

        """

        self.initialized_exchange_wrappers = initialized_exchange_wrappers
        self.summoner_configuration = summoner_configuration

    @property
    def initialized_exchange_wrappers(self):
        """
        ICryptoDataSummoner _initialized_exchange_wrappers getter.

        Returns:
            Returns _initialized_exchange_wrappers dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        return _initialized_exchange_wrappers

    @initialized_exchange_wrappers.setter
    def initialized_exchange_wrappers(self, initialized_exchange_wrappers):
        """
        ICryptoDataSummoner _initialized_exchange_wrappers setter.

        Args:
            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ICryptoDataSummoner
             will request for data from different exchanges.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """
        # TODO: validate initialized_exchange_wrappers content
        self._initialized_exchange_wrappers = initialized_exchange_wrappers

    @property
    @abstractmethod
    def summoner_configuration(self):
        """
        ICryptoDataSummoner _summoner_configuration getter.

        Returns:
            Returns _summoner_configuration dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @summoner_configuration.setter
    @abstractmethod
    def summoner_configuration(self, summoner_configuration):
        """
        ICryptoDataSummoner _summoner_configuration setter.

        Args:
        summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @abstractmethod
    async def summon(self, initialized_exchange_wrappers, summoner_configuration):
        """
        ICryptoDataSummoner summon method.

        This method will execute the concrete
         implementation of ICryptoDataSummoner and request
         data from initialized exchange wrappers.

        Args:
            summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ICryptoDataSummoner
             will request for data from different exchanges.

        Returns:
            Returns (or yields) the summoned data.

        Raises:
            ValueError: if summoner_configuration does
            not meet required configurations.

        """

async def main():
    import random

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

    tis = TestICryptoDataSummoner({'a': 1}, {'intervals': 1})
    logger.info(tis)
    async for data in tis.summon():
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
