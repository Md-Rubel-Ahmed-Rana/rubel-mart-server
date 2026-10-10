from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File
)
from uuid import UUID
from app.dependencies.auth import (
    get_current_user
)
from app.utils.response import (
    success_response
)
from app.core.database import get_db
from app.exceptions.api_exception import ApiException
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

@router.get("/")
async def get_all_categories(
    db: Session = Depends(get_db)
):
    try:
        categories = await CategoryService.get_all_categories(db)
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

@router.get("/{id}")
async def get_category_by_id(
    id: UUID,
    db: Session = Depends(get_db),
):
    category = await CategoryService.get_category_by_id(
        db=db,
        category_id=id,
    )

    return success_response(
        message="Category retrieved successfully",
        data={
            "category": {
                "id": str(category.id),
                "name":  category.name,
                "slug":  category.slug,
                "image": category.image.url if category.image_id else None,
                "description": category.description,
                "is_active":  category.is_active,
                "sort_order": category.sort_order,
                "created_at":  category.created_at,
                "updated_at": category.updated_at
            }
        },
    )

@router.patch("/{id}/image")
async def update_category_image(
    id: UUID,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    category = await CategoryService.update_category_image(
        db=db,
        id=id,
        user_id=current_user["id"],
        file=image,
    )

    return success_response(
        message="Category image updated successfully",
        data={
            "id": str(category.id),
            "image": category.image.url if category.image else None,
        },
    )
