from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from uuid import UUID
from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.exceptions.api_exception import ApiException
from app.schemas.brand_schema import CreateBrandSchema
from app.schemas.brand_schema import UpdateBrandSchema
from app.services.brand_service import BrandService
from app.utils.response import (
    success_response
)


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
    
@router.get("/{id}")
async def get_brand_by_id(
    id: UUID,
    db: Session = Depends(get_db),
):
    brand = await BrandService.get_brand_by_id(
        db=db,
        brand_id=id,
    )
    return success_response(
        message="Brand retrieved successfully",
        data= brand,
    )

@router.patch("/{id}")
async def update_brand(
    payload: UpdateBrandSchema,
    id: UUID,
    db: Session = Depends(get_db),
):
    brand = await BrandService.update_brand(
        db=db,
        brand_id=id,
        payload=payload
    )

    return success_response(
        message="Brand updated successfully",
        data= brand,
    )

@router.patch("/{id}/logo")
async def update_brand_logo(
    id: UUID,
    logo: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    brand = await BrandService.update_brand_logo(
        db=db,
        id=id,
        user_id=current_user["id"],
        logo=logo,
    )

    return success_response(
        message="Brand logo updated successfully",
        data={
            "id": str(brand.id),
            "logo_url": brand.logo.url if brand.logo_id else None,
        },
    )

@router.delete("/{id}")
async def delete_brand(
    id: UUID,
    db: Session = Depends(get_db),
):
    await BrandService.delete_brand(
        db=db,
        brand_id=id,
    )

    return success_response(
        message="Brand deleted successfully",
        data= {},
    )
