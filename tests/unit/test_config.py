"""
    Test class for config package in crypto_summoner project.
"""

import os
import unittest

from crypto_summoner.config.config import Config


class TestConfig(unittest.TestCase):

    CRYPTO_SUMMONER_CONFIG_FILE = "unit/fixtures/test_configuration.yaml"
    CRYPTO_SUMMONER_CONFIG_FILE_UNVALID = "unit/fixtures/test_configuration_unvalid"

    def setUp(self):
        pass

    def test_decrypt_configuration(self):
        config_file_path = self.CRYPTO_SUMMONER_CONFIG_FILE
        result = Config.decrypt_configuration(config_file_path)
        expected = "---\n- sampleExchangeWrapper:\n    API_KEY: sample_key\n\
                API_SECRET: sample_secret\n- NoExchangeWrapper:\n    NO_KEY: no_key    \n..."
        self.assertEqual(result, expected)

    def test_decrypt_configuration_no_existing_config_file(self):
        config_file_path = "unit/fixtures/not_existed_configuration.yaml"
        with self.assertRaises(ValueError):
            Config.decrypt_configuration(config_file_path)

    def test_obtain_configuration(self):
        os.environ["CRYPTO_SUMMONER_CONFIG_FILE"] = self.CRYPTO_SUMMONER_CONFIG_FILE
        Config.obtain_configuration()
        result = Config.CONFIGURATION
        expected = {
            "sampleExchangeWrapper": {"API_KEY": "sample_key", "API_SECRET": "sample_secret"},
            "NoExchangeWrapper": {"NO_KEY": "no_key"},
        }
        self.assertEqual(result, expected)

    def test_obtain_configuration_no_environ_set(self):
        del os.environ["CRYPTO_SUMMONER_CONFIG_FILE"]
        with self.assertRaises(ValueError):
            Config.obtain_configuration()

    def test_obtain_configuration_unvalid_config_file(self):
        os.environ["CRYPTO_SUMMONER_CONFIG_FILE"] = self.CRYPTO_SUMMONER_CONFIG_FILE_UNVALID
        with self.assertRaises(ValueError):
            Config.obtain_configuration()

    def test_get_property(self):
        os.environ["CRYPTO_SUMMONER_CONFIG_FILE"] = self.CRYPTO_SUMMONER_CONFIG_FILE
        result = Config.get_property("sampleExchangeWrapper")
        expected = {"API_KEY": "sample_key", "API_SECRET": "sample_secret"}
        self.assertEqual(result, expected)

    def test_get_property_invalid_name(self):
        os.environ["CRYPTO_SUMMONER_CONFIG_FILE"] = self.CRYPTO_SUMMONER_CONFIG_FILE
        result = Config.get_property("NoExistingProperty")
        expected = None
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
