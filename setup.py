#!/usr/bin/env python

import os
from distutils.core import setup, Extension


classifiers_list = ['License :: OSI Approved :: MIT License',
                    'Development Status :: 4 - Beta']
#extensions = [Extension('csrc', sources=[os.path.abspath('crypto_summoner/csrc/binary.cpp')])]
#py_modules_list = ['crypto_summoner.crypto_summoner']
#package_dir_list = ['crypto_summoner']
setup(
    name='crypto_summoner',
    version='0.0.0b0',
    author='chetpython',
    author_email='chetpython@gmail.com',
    description='crypto_summoner by chetpython',
    #package_dir=package_dir_list,
    #py_modules=py_modules_list,
    packages=['crypto_summoner', 
            'crypto_summoner.exchange_wrappers', 
            'crypto_summoner.inteli_logger',
            'crypto_summoner.exchange_factory',
            'crypto_summoner.config',
            'crypto_summoner.symbols_interface',
            'crypto_summoner.summoner'],
    #ext_modules=extensions,
    classifiers=classifiers_list,
    scripts=['bin/crypto_summond']
)