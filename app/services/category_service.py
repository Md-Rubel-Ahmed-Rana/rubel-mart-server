from requests import Session
from app.schemas.category_schema import CreateCategorySchema
from app.repositories.category_repository import CategoryRepository
from app.utils.slugify import Slugify
from app.exceptions.api_exception import ApiException
from app.services.media_service import (
    MediaService
)
from uuid import UUID

class CategoryService:

    @staticmethod
    async def create_category(db: Session, payload: CreateCategorySchema):
        existing_category = (
                    CategoryRepository.find_by_name(
                        db,
                        payload.name
                    )
                )

        if existing_category:
            raise ApiException(
                message="Category already exists with this name. Please choose another name.",
                status_code=409
            )

        # create slug from name
        payload.slug = Slugify.makeSlug(payload.name)

        print("Payload: ", payload.model_dump())

        return CategoryRepository.create(db, payload.model_dump())


    @staticmethod
    async def get_category_by_id(db: Session, category_id: str):
        category = CategoryRepository.find_by_id(db, category_id)

        if not category:
            raise ApiException(
                message="Category not found.",
                status_code=404
            )

        return category

    @staticmethod
    async def get_all_categories(db: Session):
        categories = CategoryRepository.find_all(db)

        if not categories:
            raise ApiException(
                message="No categories found.",
                status_code=404
            )

        return {
            "categories": categories
        }

    @staticmethod
    async def update_category_image(
        db: Session,
        id: UUID,
        user_id: str,
        file,
    ):
        category = CategoryRepository.find_by_id(
            db=db,
            category_id=str(id),
        )

        if not category:
            raise ApiException(
                message="Category not found.",
                status_code=404,
            )

        media = await MediaService.upload_file(
            db=db,
            file=file,
            uploaded_by=user_id,
            folder="categories",
        )

        category = CategoryRepository.update_image(
            db=db,
            category=category,
            image_id=str(media.id),
        )

        return category

    # get categories for public api only necessary fields
    @staticmethod
    async def get_all_categories_public(db: Session):
        categories = CategoryRepository.find_all(db)

        if not categories:
            raise ApiException(
                message="No categories found.",
                status_code=404,
            )

        # Image first, then sort_order ascending
        categories.sort(
            key=lambda category: (
                not bool(category.image and category.image.url),
                category.sort_order,
            )
        )

        dto_categories = []

        for category in categories:
            dto_categories.append({
                "name": category.name,
                "slug": category.slug,
                "image_url": (
                    category.image.url
                    if category.image and category.image.url
                    else None
                ),
            })

        return {"categories": dto_categories}
