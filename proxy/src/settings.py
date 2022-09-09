import os
import configparser
from logging import INFO
from pathlib import Path


PROJECT_ROOT = Path(os.path.dirname(__file__)).parent

CONFIG_PATH = os.path.join(PROJECT_ROOT, 'src', 'conf', 'conf.ini')

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

REDIS_HOST = CONFIG['REDIS']['HOST']
REDIS_PORT = CONFIG['REDIS']['PORT']

TARGETS_ADDRESSES = CONFIG['TARGETS']['ADDRESSES'].split(', ')


REDIS_KEYS = list(
        map(
            lambda address: f"count_handling_requests_{address.split(':')[-1]}", 
            TARGETS_ADDRESSES
        )
    )

LOG_LEVEL = INFO
