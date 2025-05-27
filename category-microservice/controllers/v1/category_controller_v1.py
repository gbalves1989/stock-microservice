from fastapi import APIRouter

category_router_v1 = APIRouter()

@category_router_v1.get("/")
async def index():
    return {"Hello": "Category Microservice"}
