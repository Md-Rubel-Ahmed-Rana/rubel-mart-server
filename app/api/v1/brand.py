from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.exceptions.api_exception import ApiException
from app.schemas.brand_schema import CreateBrandSchema
from app.services.brand_service import BrandService


router = APIRouter()

@router.post("/")
async def create_brand(payload: CreateBrandSchema,
    db: Session = Depends(get_db)
):

    try:

        brand = await BrandService.create_brand(
            db,
            payload
        )

        return {
            "message": "Brand created successfully",
            "success": True,
            "status_code": 201,
            "data": {
                "id": brand.id,
                "name": brand.name,
                "slug": brand.slug
            }
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

# get all brands by admin
@router.get("/")
async def get_all_brands(
    db: Session = Depends(get_db)
):
    try:
        brands = await BrandService.get_all_brands(db)
        return {
            "message": "Brands retrieved successfully",
            "success": True,
            "status_code": 200,
            "data": brands
        }
    except ApiException as error:
        raise HTTPException(
            status_code=error.status_code,
            detail=error.message
        )