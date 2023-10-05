from fastapi import APIRouter, Query, Body
from typing import List
from models.order import Order, Criterion

router = APIRouter()

@router.post("/solution")
async def process_orders(orders: List[Order] = Body(description="Orders list of dictionaries that each represent an order.", embed=True, min_length=1), 
    criterion: Criterion = Query(description="Order criterion that indicate filter")):
    return round(sum(
        map(lambda order: order.price * order.quantity if (order.status == criterion.value) or (criterion.value == criterion.all) else 0, orders)
        ), 2)