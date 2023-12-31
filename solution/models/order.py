from xmlrpc.client import DateTime
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from uuid import uuid4
from datetime import datetime

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
    id: Optional[str] = Field(default=uuid4())
    item: str = Field(default="New Order", min_length=3, max_length=255)
    quantity: int = Field(default=0, gt=0)
    price: float = Field(default=0, ge=0, le=1000000)
    status: Status = Field(default=Status.completed)
    created_at: datetime = Field(default=datetime.now())
    
    def serialize(self):
        return {
            'id': self.id,
            'item': self.item,
            'quantity': self.quantity,
            'price': self.price,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
