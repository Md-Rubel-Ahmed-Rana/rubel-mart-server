from fastapi import APIRouter
from app.api.v1 import auth
from app.api.v1 import database
from app.api.v1 import category


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    database.router,
    prefix="/database",
    tags=["Database"]
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

api_router.include_router(
    category.router,
    prefix="/admin/categories",
    tags=["Category"]
)
 