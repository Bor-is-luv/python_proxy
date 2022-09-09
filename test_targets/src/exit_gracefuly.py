import signal
import sys
from time import sleep
from src.logs import LOGGER
from src.redis_client import redis_client
from src.settings import REDIS_KEY


class GracefulKiller:
    def __init__(self, port):
        self.port = port
        self.is_running = True
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGHUP, self.exit_gracefully)


    def exit_gracefully(self, signum, frame):
        self.is_running = False
        sleep(3)
        LOGGER.info(f'Service started on port {self.port} switched off')
        redis_client.delete(REDIS_KEY)
        sys.exit()
    
    def get_app_is_running(self):
        return self.is_running
