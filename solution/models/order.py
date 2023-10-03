from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Status(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"

class Criterion(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"
    all = "all"

class Order(BaseModel):
    id: Optional[int] = None
    item: str = Field(default="New Order", min_length=3, max_length=255)
    quantity: int = Field(default=0, gt=0)
    price: float = Field(default=0, ge=0, le=1000000)
    status: Status = None