from fastapi import APIRouter, Query, Body
from typing import List
from models.order import Order, Criterion
from redis_client.connection import redis_client
import logging

router = APIRouter()

@router.post("/solution")
async def process_orders(orders: List[Order] = Body(description="Orders list of dictionaries that each represent an order.", embed=True, min_length=1), 
    criterion: Criterion = Query(description="Order criterion that indicate filter")):
    try:
        result_cache = redis_client.get(orders)
        if result_cache:
            logging.info("Data recovered from cache.")
            return result_cache
        else:
            result = round(
                sum(
                    map(lambda order: order.price * order.quantity if (order.status == criterion.value) or (criterion.value == criterion.all) else 0, orders)
                    ), 2
                )
            redis_client.set(orders, result, ex=3600)
            logging.info("Cached data.")
            return result
    except Exception as e:
        logging.error(f"ERROR: {e}")