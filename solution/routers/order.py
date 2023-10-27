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
        input = json.dumps([item.serialize() for item in orders])
        result = redis_client.get(input)
        # REDIS ALL ITEMS ---------- [key for key in redis_client.scan_iter("*")]
        logging.info("Server connect to cache.")
    except Exception as e:
        logging.error(f"ERROR START: {e}")
    
    if result:
        logging.info("Data recovered from cache.")
        return int(result.decode('utf-8'))
    else:
        result = round(
            sum(
                map(lambda order: order.price * order.quantity if (order.status == criterion.value) or (criterion.value == criterion.all) else 0, orders)
                ), 2
            )
        try:
            keyval = json.dumps([item.serialize() for item in orders])
            redis_client.set(keyval, result, ex=300)
            logging.info("Cached data.")
        except Exception as e:
            logging.error(f"ERROR: {e}")
        finally:
            return result
