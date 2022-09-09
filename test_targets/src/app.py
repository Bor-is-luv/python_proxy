from time import sleep
from flask import Flask
from src.logs import LOGGER
from src.redis_client import redis_client
from src.settings import REDIS_KEY, PORT
from src.exit_gracefuly import GracefulKiller


app = Flask(__name__)

gracefull_killer = GracefulKiller(PORT)
redis_client.set(REDIS_KEY, 0)


@app.route("/")
def root_route():
    if gracefull_killer.get_app_is_running():
        redis_client.incr(REDIS_KEY)
        # some work
        sleep(1)

        redis_client.decr(REDIS_KEY)
        return "<p>Hello, World!</p>", 200
    else:
        return "<p>Temporary unavailable</p>", 503


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
