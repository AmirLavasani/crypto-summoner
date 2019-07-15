"""
    GeneralCryptoDataSummoner is a concrete implementations of
    ICryptoDataSummoner for retrieving exchange data from
    different IExchangeWrapper concrete implementations.

    GeneralCryptoDataSummoner tasked with gathering all prices
     from all initialized exchange wrappers. It has a relatively
     medium intervals for retrieving data compared to other concrete
     implementations of ICryptoDataSummoner.

"""

import asyncio

from crypto_summoner.crypto_data_summoner.icrypto_data_summoner import ICryptoDataSummoner
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('GeneralCryptoDataSummoner')


class GeneralCryptoDataSummoner(ICryptoDataSummoner):
    """
    GeneralCryptoDataSummoner Class

    GeneralCryptoDataSummoner is a concrete implementations of
    ICryptoDataSummoner for retrieving exchange data from
    different IExchangeWrapper concrete implementations.

    GeneralCryptoDataSummoner tasked with gathering all prices
     from all initialized exchange wrappers. It has a relatively
     medium intervals for retrieving data compared to other concrete
     implementations of ICryptoDataSummoner.

    Design Pattern:

    ...

    Attributes:
        initialized_exchange_wrappers (dic):
         The initialized dictionary of
         exhcange wrappers. Using this dictionary the
         concrete implementation of GeneralCryptoDataSummoner
         will request for data from different exchanges.

        summoner_configuration (dic): a dictionary for the
         summoner execution configuration. It should contain
         'intervals' keyword. 'intervals' value is used for the
         intervals to retrieve data.

    Methods:
        summon(self, initialized_exchange_wrappers, summoner_configuration):
         This method will execute the concrete implementation of
         GeneralCryptoDataSummoner and request data from initialized
         exchange wrappers.

    """

    def __init__(self, initialized_exchange_wrappers, summoner_configuration):
        """
        Inits GeneralCryptoDataSummoner with initialized_exchange_wrappers
         and summoner_configuration.

        According to ICryptoDataSummoner we should call super init in
         derived __init__ functions.

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
             the concrete implementation of GeneralCryptoDataSummoner
             will request for data from different exchanges.

            summoner_configuration (dic): a dictionary for the
             summoner execution configuration. It should contain
             'intervals' keyword. 'intervals' value is used for the
             intervals to retrieve data.

        """

        ICryptoDataSummoner.__init__(self, initialized_exchange_wrappers, summoner_configuration)

    @property
    def summoner_configuration(self):
        """
        GeneralCryptoDataSummoner _summoner_configuration getter.

        Returns:
            Returns _summoner_configuration dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        return self._summoner_configuration

    @summoner_configuration.setter
    def summoner_configuration(self, summoner_configuration):
        """
        GeneralCryptoDataSummoner _summoner_configuration setter.

        Args:
        summoner_configuration (dic): a dictionary
             for the summoner execution configuration.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        if "intervals" not in summoner_configuration:
            raise ValueError(f"summoner_configuration is not valid for {__class__.__name__}")
        self._summoner_configuration = summoner_configuration

    async def summon(self):
        """
        GeneralCryptoDataSummoner summon method.

        This method will request data from initialized
         exchange wrappers in specified intervals.

        Returns:
            Returns (or yields) the summoned data.

        """

        while True:
            data = {}
            await asyncio.sleep(self.summoner_configuration['intervals'])
            for exchange_name, exchange_wrapper in self.initialized_exchange_wrappers.items():
                data[exchange_name] = await exchange_wrapper.get_prices()
            yield data

async def main():
    from crypto_summoner.exchange_factory.general_exchange_factory import GeneralExchangeFactory

    gef = GeneralExchangeFactory()
    gef.register_all_exchanges()
    await gef.create_all_exchanges()

    gcds = GeneralCryptoDataSummoner(gef.initialized_exchange_wrappers, {'intervals': 10})

    logger.info(gcds)
    async for data in gcds.summon():
        for name, prices in data.items():
            out = f"exchange_name:\t{name}\nprices:\t{prices}\n"
            logger.info(out)

if __name__ == "__main__":
    asyncio.run(main())
