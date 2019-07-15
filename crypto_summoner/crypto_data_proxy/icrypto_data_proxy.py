"""
    ICryptoDataProxy is an abstract class bridging different
     crypto data summoners to different crypto data preservers.

    Any kind of proxy class for bridging an ICryptoDataSummoner
     concrete implementation and a ICryptoDataPreserver concrete
     implementation should inherit from ICryptoDataProxy.

"""

from abc import ABC, abstractmethod
import asyncio

from crypto_summoner.crypto_data_summoner.icrypto_data_summoner import ICryptoDataSummoner
from crypto_summoner.crypto_data_preserver.icrypto_data_preserver import ICryptoDataPreserver
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger('ICryptoDataProxy')


class ICryptoDataProxy(ABC):
    """
    ICryptoDataProxy is an abstract class bridging different
     summoners to different crypto data preservers.

    Any kind of proxy class for bridging an ICryptoDataProxy
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
        Inits ICryptoDataProxy with _crypto_data_summoner
         and _crypto_data_preserver.

        Call this init in derived __init__ functions.
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

        self.crypto_data_summoner = crypto_data_summoner
        self.crypto_data_preserver = crypto_data_preserver
        self._bind = False

    @property
    def crypto_data_summoner(self):
        """
        ICryptoDataProxy _crypto_data_summoner getter.

        Returns:
            Returns _crypto_data_summoner.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        return self._crypto_data_summoner

    @crypto_data_summoner.setter
    def crypto_data_summoner(self, crypto_data_summoner):
        """
        ICryptoDataProxy _crypto_data_summoner setter.

        Args:
            crypto_data_summoner (ICryptoDataSummoner): a concrete
             implementation of ICryptoDataSummoner abstract class.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        assert isinstance(crypto_data_summoner, ICryptoDataSummoner), \
            "object is not inherited from ICryptoDataSummoner."
        self._crypto_data_summoner = crypto_data_summoner

    @property
    def crypto_data_preserver(self):
        """
        ICryptoDataProxy _crypto_data_preserver getter.

        Returns:
            Returns _crypto_data_preserver dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        return self._crypto_data_preserver

    @crypto_data_preserver.setter
    def crypto_data_preserver(self, crypto_data_preserver):
        """
        ICryptoDataProxy _crypto_data_preserver setter.

        Args:
            crypto_data_preserver (ICryptoDataPreserver): a concrete
             implementation of ICryptoDataPreserver abstract class.

        Returns:
            Returns nothing.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        assert isinstance(crypto_data_preserver, ICryptoDataPreserver), \
            "object is not inherited from ICryptoDataPreserver."
        self._crypto_data_preserver = crypto_data_preserver

    def bind(self):
        """
        ICryptoDataProxy bind method.

        This method will bind a concrete implementation
         of ICryptoDataSummoner to a concrete implementation
         of ICryptoDataPreserver.

        Returns:
            Returns nothing.

        """

        self._bind = True

    def unbind(self):
        """
        ICryptoDataProxy unbind method.

        This method will unbind a concrete implementation
         of ICryptoDataSummoner from a concrete implementation
         of ICryptoDataPreserver.

        Returns:
            Returns nothing.

        """

        self._bind = False

    @abstractmethod
    async def connect(self):
        """
        ICryptoDataProxy connect method.

        This method will bind and connect _crypto_data_summoner to
         _crypto_data_preserver and pass through data from summoner
          to be preserver.
        """


async def main():

    class TestICryptoDataProxy(ICryptoDataProxy):
        def __init__(self, crypto_data_summoner, crypto_data_preserver):
            ICryptoDataProxy.__init__(self, crypto_data_summoner, crypto_data_preserver)

        async def connect(self):
            pass

    cdp = TestICryptoDataProxy({}, {})
    logger.info(cdp)


if __name__ == "__main__":
    asyncio.run(main())
