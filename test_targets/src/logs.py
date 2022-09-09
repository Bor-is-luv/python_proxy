import logging

from src.settings import LOG_LEVEL


logging.basicConfig(level=LOG_LEVEL)
LOGGER = logging.getLogger("Target server")