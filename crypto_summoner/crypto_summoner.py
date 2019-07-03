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
        att (str): optional. A sample class attribute for docstring
         (defaualt is 'sample_attribute_for_docstring')

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

    @staticmethod
    def dev_build_status():
        """
        CryptoSummoner package status after installation.

        It will report the last dev build status generated
            by integration test.

        Returns:
            Returns nothing. Only logs status.

        """

        import os
        with open("crypto_summoner/status", "r") as f:
            status = f.read()
        if "successfull" in status:
            logger.info(status)
        else:
            logger.error(status)

        command = r"find crypto_summoner -type f | xargs -I {} wc -l {} | grep -v __pycache__\
             | cut -d ' ' -f1 | awk '{s+=$1} END {print s}'"
        lines_count = os.popen(command).read()

        logger.info(f"Number of lines:\t {lines_count}")
