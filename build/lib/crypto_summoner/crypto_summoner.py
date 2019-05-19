"""
    Main class of crypto_summoner package.
    
    This package will gather live data from crypto exchanges, 
    and insert data into a time-series database.

"""

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('CryptoSummoner')

class CryptoSummoner:
    """
    CryptoSummoner Class

    ...

    Attributes:
        att (str): optional. A sample class attribute for docstring (defaualt is 'sample_attribute_for_docstring')
        name (str): optional. The name of the class (defaualt is 'CryptoSummoner')
    
    Methods:
        status(sound=None): Prints 'Package works!' for setup installation purpose.
    """

    att = "sample_attribute_for_docstring"

    def __init__(self, name="CryptoSummoner"):
        """
        Inits CryptoSummoner with name.
        
        Args:        
            name (str): optional. The name of the class (defaualt is 'CryptoSummoner')
        """

        self.name = name
    
    @staticmethod
    def status(msg="Package works!"):
        """
        CryptoSummoner package status after installation.
        
        Args:
            msg (str): optional. The message to print (default is 'Package works!')
        
        Returns:
            Returns nothing. Only prints the msg.
        
        Raises:
            ValueError: If msg is None or empty
        """

        if msg is None or msg == '':
            raise ValueError("msg parameter can not be None or empty.")
        
        logger.info(msg)
