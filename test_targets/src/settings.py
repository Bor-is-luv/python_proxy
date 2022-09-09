import os
import configparser
from logging import INFO
from pathlib import Path

from src.cli_params import *


PROJECT_ROOT = Path(os.path.dirname(__file__)).parent

CONFIG_PATH = os.path.join(PROJECT_ROOT, 'src', 'conf', 'conf.ini')

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

REDIS_HOST = CONFIG['REDIS']['HOST']
REDIS_PORT = CONFIG['REDIS']['PORT']
REDIS_KEY = f'count_handling_requests_{PORT}'

LOG_LEVEL = INFO