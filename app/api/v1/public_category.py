from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.exceptions.api_exception import ApiException
from app.services.category_service import CategoryService


router = APIRouter()


@router.get("/")
async def get_all_categories_public(
    db: Session = Depends(get_db)
):
    try:
        categories = await CategoryService.get_all_categories_public(db)
        return {
            "message": "Categories retrieved successfully",
            "success": True,
            "status_code": 200,
            "data": categories
        }
    except ApiException as error:
        raise HTTPException(
            status_code=error.status_code,
            detail=error.message
        )