from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.category_schema import CreateCategorySchema
from app.services.category_service import CategoryService


router = APIRouter()

@router.post("/")
async def create_category(payload: CreateCategorySchema,
    db: Session = Depends(get_db)
):

    try:

        category = await CategoryService.create_category(
            db,
            payload
        )

        return {
            "message": "Category created successfully",
            "success": True,
            "status_code": 201,
            "data": {
                "id": category.id,
                "name": category.name,
                "slug": category.slug
            }
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )