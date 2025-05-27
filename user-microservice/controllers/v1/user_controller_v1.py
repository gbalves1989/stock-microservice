from fastapi import APIRouter

user_router_v1 = APIRouter()

@user_router_v1.get("/")
async def index():
    return {"Hello": "User Microservice"}
