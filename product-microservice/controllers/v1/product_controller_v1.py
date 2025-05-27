from fastapi import APIRouter

product_router_v1 = APIRouter()

@product_router_v1.get("/")
async def index():
    return {"Hello": "Product Microservice"}
