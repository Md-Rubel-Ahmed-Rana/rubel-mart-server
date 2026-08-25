from requests import Session
from app.repositories.brand_repository import BrandRepository
from app.schemas.brand_schema import CreateBrandSchema
from app.utils.slugify import Slugify
from app.exceptions.api_exception import ApiException


class BrandService:

    @staticmethod
    async def create_brand(db: Session, payload: CreateBrandSchema):
        existing_brand = (
                    BrandRepository.find_by_name(
                        db,
                        payload.name
                    )
                )

        if existing_brand:
            raise ApiException(
                message="Brand already exists with this name. Please choose another name.",
                status_code=409
            )

        # create slug from name
        payload.slug = Slugify.makeSlug(payload.name)

        print("Payload: ", payload.model_dump())

        return BrandRepository.create(db, payload.model_dump())


    @staticmethod
    async def get_brand_by_id(db: Session, brand_id: str):
        brand = BrandRepository.find_by_id(db, brand_id)

        if not brand:
            raise ApiException(
                message="Brand not found.",
                status_code=404
            )

        return brand

    @staticmethod
    async def get_all_brands(db: Session):
        brands = BrandRepository.find_all(db)

        if not brands:
            raise ApiException(
                message="No brands found.",
                status_code=404
            )

        return brands

    # get brands for public api only necessary fields
    @staticmethod
    async def get_all_brands_public(db: Session):
        brands = BrandRepository.find_all(db)

        if not brands:
            raise ApiException(
                message="No brands found.",
                status_code=404
            )
        dto_brands = []
        for brand in brands:
            dto_brands.append({
                "name": brand.name,
                "slug": brand.slug,
                "logo_url": brand.logo.url if brand.logo and brand.logo.url else None
            })
        return dto_brands