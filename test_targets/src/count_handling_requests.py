import schedule
from src.redis_client import redis_client
from src.logs import LOGGER
from src.settings import REDIS_KEY



def count_handling_requests():
    count_requests = redis_client.get(REDIS_KEY)
    LOGGER.info(f'{REDIS_KEY} equals {count_requests}')


if __name__ == "__main__":
    check_count_handling_requests = schedule.every(10).seconds.do(count_handling_requests)
    while True:
        schedule.run_pending()
