from fastapi import APIRouter, Query, Body
from typing import List
from models.order import Order, Criterion
from redis_client.connection import redis_client
import json
import logging

router = APIRouter()

@router.post("/solution")
async def process_orders(orders: List[Order] = Body(description="Orders list of dictionaries that each represent an order.", embed=True, min_length=1), 
    criterion: Criterion = Query(description="Order criterion that indicate filter")):
    result = None
    try:
        result = redis_client.get(json.loads(orders))
        print(f'********** REDIS ORDER ********** {result}')
        logging.info("Server connect to cache.")
    except Exception as e:
        print(f"ERROR: {e}")
        logging.error(f"ERROR START: {e}")
    
    if result:
        logging.info("Data recovered from cache.")
        print(f'YES: {result}')
        return result
    else:
        result = round(
            sum(
                map(lambda order: order.price * order.quantity if (order.status == criterion.value) or (criterion.value == criterion.all) else 0, orders)
                ), 2
            )
        try:
            redis_client.set(json.dumps(orders, default=vars), json.dumps(result, default=vars), ex=3600)
            logging.info("Cached data.")
        except Exception as e:
            print(f"ERROR END: {e}")
            logging.error(f"ERROR: {e}")
        finally:
            return result
