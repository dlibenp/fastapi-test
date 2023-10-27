import redis
#from redis import Redis
from redis.exceptions import ConnectionError
#from os import getenv
import os
import logging

try:
    #redis_client = Redis(
    #    host=getenv("REDIS_HOST"),
    #    port=getenv("REDIS_PORT"),
    #    password=getenv("REDIS_PASSWORD"),
    #    db=getenv("REDIS_DB"),
    #    ssl=bool(getenv("REDIS_SSL"))
    #)
    redis_client = redis.from_url(os.environ['REDIS_URL'])
    print(f'*********** REDIS CLIENT *********** {os.environ['REDIS_URL']}')
    logging.info("CONNECTED TO REDIS!!")
except ConnectionError as cx:
    logging.error(f"CONNECTION ERROR: {cx}")
except Exception as ex:
    logging.error(f"ERROR: {ex}")
