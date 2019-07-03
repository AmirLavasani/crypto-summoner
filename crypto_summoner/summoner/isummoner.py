"""
    ISummoner is an abstract class for retrieving
     exchange data from different IExchangeWrapper
     concrete implementations.

    Any kind of data request for retrieving data from
     IExchangeWrapper implementations concrete should
     inherit from ISummoner.

"""

from abc import ABC, abstractmethod
import asyncio

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('ISummoner')


class ISummoner(ABC):
    """
    ISummoner Class

    ISummoner is an abstract class for initializing
     ISummoner concrete implementations.

    Any kind of data request for retrieving data from
     IExchangeWrapper implementations concrete should
     inherit from ISummoner.

    Design Pattern:

    ...

    Attributes:
        _initialized_exchange_wrappers (dic): Dictionary
         of names and classes which inherited from
         IExchangeWrapper class and initialized.

    Methods:
        register_exchange
         (self, exchange_name, exchange_wrapper_class_reference):
         Registers an IExchangeWrapper concrete implementation class.

    """

    def __init__(self):
        """
        Inits ISummoner with initialized_exchange_wrappers
         and summoner_configuration.

        Call this init in derived __init__ functions.
        class derived(ISummoner):
            def __init():
                ISummoner.__init__(self,
                                    initialized_exchange_wrappers,
                                    summoner_configuration
                                )
        Attributes:
            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ISummoner
             will request for data from different exchanges.

            summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

        """

        self._initialized_exchange_wrappers = {}
        self._summoner_configuration = {}

    @property
    @abstractmethod
    def initialized_exchange_wrappers(self):
        """
        ISummoner _initialized_exchange_wrappers getter.

        Returns:
            Returns _initialized_exchange_wrappers dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @initialized_exchange_wrappers.setter
    @abstractmethod
    def initialized_exchange_wrappers(self, initialized_exchange_wrappers):
        """
        ISummoner _initialized_exchange_wrappers setter.

        Args:
            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ISummoner
             will request for data from different exchanges.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

    @property
    @abstractmethod
    def summoner_configuration(self):
        """
        ISummoner _summoner_configuration getter.

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
        ISummoner _summoner_configuration setter.

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
        ISummoner summon method.

        This method will execute the concrete
         implementation of ISummoner and request
         data from initialized exchange wrappers.

        Args:
            summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

            initialized_exchange_wrappers (dic):
             The initialized dictionary of
             exhcange wrappers. Using this dictionary
             the concrete implementation of ISummoner
             will request for data from different exchanges.

        Returns:
            Returns (or yields) the summoned data.

        Raises:
            ValueError: if summoner_configuration does
            not meet required configurations.

        """

async def main():
    import random

    class TestISummoner(ISummoner):
        def __init__(self):
            ISummoner.__init__(self)

        @property
        def initialized_exchange_wrappers(self):
            return self._initialized_exchange_wrappers

        @initialized_exchange_wrappers.setter
        def initialized_exchange_wrappers(self, initialized_exchange_wrappers):
            print('1')
            self._initialized_exchange_wrappers = initialized_exchange_wrappers

        @property
        def summoner_configuration(self):
            return self._summoner_configuration

        @summoner_configuration.setter
        def summoner_configuration(self, summoner_configuration):
            if "intervals" not in summoner_configuration:
                raise ValueError(f"summoner_configuration is not valid for {__class__.__name__}")
            self._summoner_configuration = summoner_configuration

        async def summon(self, initialized_exchange_wrappers, summoner_configuration):
            self.initialized_exchange_wrappers = initialized_exchange_wrappers
            self.summoner_configuration = summoner_configuration
            while True:
                await asyncio.sleep(self.summoner_configuration['intervals'])
                yield random.randint(1, 100)

    tis = TestISummoner()
    logger.info(tis)
    async for data in tis.summon({'a': 1}, {'intervals': 1}):
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
