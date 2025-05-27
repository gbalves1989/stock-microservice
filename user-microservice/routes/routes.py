from fastapi import APIRouter
from controllers.v1 import user_controller_v1
from core.config import settings

api_router = APIRouter()

api_router.include_router(
    user_controller_v1.user_router_v1,
    prefix="/v1/users",
    tags=["Users"]
)
    