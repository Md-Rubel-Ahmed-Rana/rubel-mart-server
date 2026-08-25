from requests import Session
from app.schemas.category_schema import CreateCategorySchema
from app.repositories.category_repository import CategoryRepository
from app.utils.slugify import Slugify
from app.exceptions.api_exception import ApiException


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