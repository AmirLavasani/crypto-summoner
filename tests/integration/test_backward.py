"""
    Test class for backward compatibility of program.
"""

import os
import unittest

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('TestBackward')



class TestBackward(unittest.TestCase):
    """
    TestBackward class

    Test class for backward compatibility of program.

    Inherited from unittest.TestCase.
    It will run the integeration test backwardly
    till the most recent development state.

        ...

    Attributes:
        _CRYPTO_SUMMONER_CONFIG_FILE (str): 
            The path to the configuration file.
    
    Methods:
        setUp(self): unittest setUp function. Setup 
            required system state, before running backward.

    """

    _CRYPTO_SUMMONER_CONFIG_FILE = "crypto_summoner/config/configuration.yaml"
    
    def setUp(self):
        """
            unittest setUp function.

            Setup required system state, before running 
                backward. Testing Framework will automatically
                this function call for every single test we run.

            Returns:
            Returns Nothing.

            Raises:
                Any exception raised by this method will be 
                    considered an error rather than a test failure.
        """

        # conda_path = "/home/amir/miniconda3/bin/activate"
        # os.system(f"source {conda_path} cp")
        # logger.info("Conda environment activated.")


        os.system("python setup.py install")
        logger.info("crytpo_summoner installed.")

        os.environ['CRYPTO_SUMMONER_CONFIG_FILE'] = self._CRYPTO_SUMMONER_CONFIG_FILE
        logger.info("Configuration set.")


    def test_latest_dev_state_integration(self):
        self._general_exchange_factory_integration()
    
    def _general_exchange_factory_integration(self):
        """
            test_general_exchange_factory_integration method.

            call general_exchange_factory with __name__ = "__main__"

        """

        os.system("python crypto_summoner/exchange_factory/general_exchange_factory.py")


if __name__ == "__main__":
    unittest.main()
