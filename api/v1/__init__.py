from fastapi import APIRouter
from .category import gender_router

__all__ = ["router"]
router = APIRouter(
    prefix="/v1"
)
router.include_router(router=gender_router.router)
