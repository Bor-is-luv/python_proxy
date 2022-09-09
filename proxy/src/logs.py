import logging
from sys import stdout

from src.settings import LOG_LEVEL

LOG_FORMAT = {
    'host': '%(hostname)s',
    'where': '%(module)s.%(funcName)s',
    'stack_trace': '%(exc_text)s',
    'level_name': '%(levelname)s',
    'log': '%(processName)s-%(threadName)s-%(filename)s:%(lineno)s-%(module)s-%(funcName)s',
}


logging.basicConfig(level=LOG_LEVEL)
LOGGER = logging.getLogger("Proxy server")