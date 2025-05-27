from fastapi import APIRouter
from controllers.v1 import category_controller_v1
from core.config import settings

api_router = APIRouter()

if settings.API_VERSION == "v1":
    api_router.include_router(
        category_controller_v1.category_router_v1,
        prefix=f"/${settings.API_VERSION}/categories",
        tags=["Categories"]
    )
    