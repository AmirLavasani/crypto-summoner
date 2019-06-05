"""
    Config is a class for accessing an encrypted config file.
    
    It will decrypt the YAML config file and provides other classes with their configurations.

"""

import os

import yaml

from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('Config')


class Config:
    """
    Config class
    
    Config is a class for accessing and storing an encrypted config file.    
    It will decrypt the YAML config file and provides other classes with their configurations.
    Design Pattern: Configuration :D

    ...

    Attributes:
        CONFIGURATION (dic): Dictionary of key values.
    
    Methods:       
        get_property(cls, property_name): Returns the value of requested property_name.
        decrypt_configuration(cls): Decrypt configuration file and set class CONFIGURATION member.
    """
    CONFIGURATION = {}       

    @classmethod  
    def get_property(cls, property_name):
        """
        Returns the value of requested property_name.
        
        Args:
            property_name (str): Name of property.
        
        Returns:
            If successfull returns a property value, otherwise None.
        """
        
        # obtain and set configuration data one time.
        if cls.CONFIGURATION == {}:
            cls.obtain_configuration()
        
        if property_name not in cls.CONFIGURATION.keys():
            return None
        return cls.CONFIGURATION[property_name]

    @classmethod
    def obtain_configuration(cls):
        """
        Obtain configuration data and set CONFIGURATION class member.

        It assumes an environment variable CRYPTO_SUMMONER_CONFIG_FILE is set to YAML configuration file.
        
        Returns:
            Returns nothing.
        
        Raises:
            ValueError: This function must be override in derived classes  
        """
        if "CRYPTO_SUMMONER_CONFIG_FILE" not in os.environ:
            logger.exception("CRYPTO_SUMMONER_CONFIG_FILE environment variable is not set.")
            raise ValueError("CRYPTO_SUMMONER_CONFIG_FILE environment variable is not set.")
        
        yaml_config_file = os.getenv("CRYPTO_SUMMONER_CONFIG_FILE")
        decrypted_config_data = cls.decrypt_configuration(yaml_config_file)

        try:
            yaml_configs = yaml.safe_load(decrypted_config_data)
        except yaml.YAMLError:
            logger.exception("Failed to safe_load config file.")
            raise ValueError("Failed to safe_load config file.")

        # yaml_configs is a list of dictionaries
        for config in yaml_configs:           
            cls.CONFIGURATION.update(config)

    @classmethod
    def decrypt_configuration(cls, yaml_config_file):
        """
        Decrypt configuration data and return the data.        
        
        Args:
            yaml_config_file (str): YAML configuration file path.

        Returns:
            Returns configuration data.
        
        Raises:
            ValueError: If Configuration YAML file not exists.
            # TODO raise if it can not decrypt data or decryption key is not valid.
        """

        if not os.path.exists(yaml_config_file):
            raise ValueError("Configuration YAML file not exists.")

        with open(yaml_config_file, 'r') as file:
            config_data = file.read()
        # TODO encrypt and decrypt yaml file
        return config_data


def main():
    Config.obtain_configuration()
    print(Config.CONFIGURATION)

if __name__ == "__main__":
    main()