from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv
import logging

try:
    redis_client = Redis(
        host=getenv("REDIS_HOST"),
        port=getenv("REDIS_PORT"),
        password=getenv("REDIS_PASSWORD"),
        db=getenv("REDIS_DB"),
        ssl=bool(getenv("REDIS_SSL"))
    )
    logging.info("CONNECTED TO REDIS!!")
except ConnectionError as cx:
    logging.error(f"CONNECTION ERROR: {cx}")
except Exception as ex:
    logging.error(f"ERROR: {ex}")