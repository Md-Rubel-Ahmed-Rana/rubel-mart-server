from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.exceptions.api_exception import ApiException
from app.services.brand_service import BrandService


router = APIRouter()


@router.get("/")
async def get_all_brands_public(
    db: Session = Depends(get_db)
):
    try:
        brands = await BrandService.get_all_brands_public(db)
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