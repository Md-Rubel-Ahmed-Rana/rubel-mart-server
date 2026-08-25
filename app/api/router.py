from fastapi import APIRouter
from app.api.v1 import auth
from app.api.v1 import database
from app.api.v1 import category
from app.api.v1 import public_category
from app.api.v1 import brand
from app.api.v1 import public_brand


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
 

api_router.include_router(
    public_category.router,
    prefix="/categories",
    tags=["Category"]
)

api_router.include_router(
    brand.router,
    prefix="/admin/brands",
    tags=["Brand"]
)
 

api_router.include_router(
    public_brand.router,
    prefix="/brands",
    tags=["Brand"]
)
 