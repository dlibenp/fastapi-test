from fastapi import APIRouter
from typing import List
from models.order import Order, Criterion

router = APIRouter()

@router.post("/solution")
async def process_orders(orders: List[Order], criterion: Criterion):
    return round(sum(
        map(lambda order: order.price * order.quantity if (order.status == criterion.value) or (criterion.value == criterion.all) else 0, orders)
        ), 2)