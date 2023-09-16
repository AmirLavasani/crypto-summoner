"""
    InfluxCryptoDataPreserver is a concrete implementation of
     ICryptoDataPreserver for preserving data gathered from
     a summoner and insert it into InfuxDB - a time series data base.

    Any kind of preserver class for preserving data
     from a concrete implementation of a ISummoner should
     inherit from ICryptoDataPreserver.

"""

import asyncio

from influxdb import InfluxDBClient

from crypto_summoner.crypto_data_preserver.icrypto_data_preserver import ICryptoDataPreserver
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger

logger = InteliLogger.get_logger("InfluxCryptoDataPreserver")


class InfluxCryptoDataPreserver(ICryptoDataPreserver):
    """
    InfluxCryptoDataPreserver is a concrete implementation of
     ICryptoDataPreserver for preserving data gathered from
     a summoner and insert it into InfuxDB - a time series data base.

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
        Inits InfluxCryptoDataPreserver.

        Call this init in derived __init__ functions.
        class derived(ICryptoDataPreserver):
            def __init():
                ICryptoDataPreserver.__init__(self, preserver_configuration)

        Attributes:
            preserver_configuration (dic): a dictionary
             for the preserver configurations.

        """

        ICryptoDataPreserver.__init__(self, preserver_configuration)
        self.influxdbClient = InfluxDBClient(
            host="127.0.0.1", port=8086, username="admin", password="67J2SqMOWp", database="cryptoData"
        )

    @property
    def preserver_configuration(self):
        """
        ICryptoDataSummoner _preserver_configuration getter.

        Returns:
            Returns _preserver_configuration dictionary.

        Raises:
            NotImplementedError: This function must be
             override in derived classes

        """

        return self._preserver_configuration

    @preserver_configuration.setter
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
        # TODO Validate preserver_configuration
        self._preserver_configuration = preserver_configuration

    async def on_data(self, data):
        """
        InfluxCryptoDataPreserver on_data method.

        This method is called from a ICryptoDataProxy concrete
         implementation when new data is available.

        Args:
        data (dic): a dictionary of the ICryptoDataSummoner
         standard summoned data.

        Returns:
            Returns nothing.

        """

        # TODO Validate data
        # TODO Change format of data
        influx_friendly = self.convert_data_influxdb(data)
        self.influxdbClient.write_points(influx_friendly)
        logger.info("Data points inserted into influxdb.")

    def convert_data_influxdb(self, data):
        """
        InfluxCryptoDataPreserver convert_data_influxdb method.

        This method is used for converting standard data format of
         an ICryptoDataSummoner into an influxdb-friendly json.

        A ICryptoDataSummoner will return data in the following format:
        data = {
            "BinanceExchange":
                [
                    {
                        "symbol": "LTCBTC",
                        "price": "4.00000200"
                    },
                    {
                        "symbol": "ETHBTC",
                        "price": "0.07946600"
                    }
                ]
            "KrakenExchange":
                [
                    {
                        "symbol": "LTCBTC",
                        "price": "4.00000600"
                    },
                    {
                        "symbol": "ETHBTC",
                        "price": "0.07846600"
                    }
                ]
            }

        We want to have Symbol as our measurements and exchange name as
         one of our tags. The price will be a field in influxdb.

        An influx friendly list to write points is as following:

        json_body = [
            {
                "measurement": "LTCBTC",
                "tags": {
                    "exchange": "BinanceExchange"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "price": 4.00000200
                }
            },
            {
                "measurement": "LTCBTC",
                "tags": {
                    "exchange": "KrakenExchange"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "price": 4.00000600
                }
            },
                    {
                "measurement": "ETHBTC",
                "tags": {
                    "exchange": "BinanceExchange"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "price": 0.07946600
                }
            },
            {
                "measurement": "ETHBTC",
                "tags": {
                    "exchange": "KrakenExchange"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "price": 0.07846600
                }
            },
        ]

        Args:
        data (dic): a dictionary of the ICryptoDataSummoner
         standard summoned data.

        Returns:
            Returns an influxdb-friendly list.

        """
        # json_template = {
        #         "measurement": "",
        #         "tags": {
        #             "exchange": ""
        #         },
        #         "fields": {
        #             "price": ""
        #         }
        #     }

        influx_friendly = []
        for exchange_name, exchange_data in data.items():
            for pair_data in exchange_data:
                json_template = {}
                json_template["measurement"] = pair_data["symbol"]
                json_template["tags"] = {}
                json_template["tags"]["exchange"] = exchange_name
                json_template["fields"] = {}
                json_template["fields"]["price"] = float(pair_data["price"])
                influx_friendly.append(json_template)
        return influx_friendly


async def main():
    import asyncio

    icdp = InfluxCryptoDataPreserver({})
    logger.info(icdp)
    data = {
        "BinanceExchange": [
            {"symbol": "LTCBTC", "price": "4.00000200"},
            {"symbol": "ETHBTC", "price": "0.07946600"},
        ],
        "KrakenExchange": [
            {"symbol": "LTCBTC", "price": "4.00000600"},
            {"symbol": "ETHBTC", "price": "0.07846600"},
        ],
    }
    while True:
        await icdp.on_data(data)
        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
