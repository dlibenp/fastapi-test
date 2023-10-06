from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv
import logging

try:
    redis_client = Redis(
        host=getenv("REDIS_HOST"),
        port=getenv("REDIS_PORT"),
        password=getenv("REDIS_PASSWORD"),
        ssl=bool(getenv("REDIS_SSL"))
    )
    logging.info("CONNECTED TO REDIS!!")
except ConnectionError as cx:
    logging.error(f"ERROR: {cx}")
except Exception as ex:
    logging.error(f"ERROR: {ex}")