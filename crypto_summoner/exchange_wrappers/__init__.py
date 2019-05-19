from crypto_summoner.exchange_wrappers.exchange_wrapper_registery import ExchangeWrapperRegistery

# Import all classes in this directory so that classes with @register_class are registered. 

from os.path import basename, dirname, join
from glob import glob
from crypto_summoner.inteli_logger.inteli_logger import InteliLogger
logger = InteliLogger.get_logger('ExchangeWrappersInit')

logger.info(f'Invoking __init__.py for {__name__}')

pwd = dirname(__file__)
for x in glob(join(pwd, '*.py')):    
    if '__' not in x:
        __import__('.'.join([f'{__name__}', basename(x).replace('.py', '')]), globals(), locals())


logger.info(f"I ExchangeWrapperRegistry imported and registered all exchange_wrappers.")
logger.info(f"It will be accessible through REGISTERED_IEXCHANGE_WRAPPER_CLASSES.")

__all__ = ['ExchangeWrapperRegistery']