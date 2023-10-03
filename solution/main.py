from fastapi import FastAPI
from routers.order import router as order_router

app = FastAPI()

app.include_router(order_router)