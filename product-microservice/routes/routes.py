from fastapi import APIRouter
from controllers.v1 import product_controller_v1
from core.config import settings

api_router = APIRouter()

if settings.API_VERSION == "v1":
    api_router.include_router(
        product_controller_v1.product_router_v1,
        prefix=f"/${settings.API_VERSION}/products",
        tags=["Products"]
    )
    