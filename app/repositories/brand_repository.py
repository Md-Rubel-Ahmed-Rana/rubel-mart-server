from sqlalchemy.orm import Session
from app.models.brand import Brand


class BrandRepository:

    @staticmethod
    def find_by_name(
            db: Session,
            name: str
        ):
    
            brand =  (
                db.query(Brand)
                .filter(Brand.name == name)  
                .first()
            )
            return brand


    
    @staticmethod
    def create(
        db: Session,
        payload: dict
    ):

        brand = Brand(**payload)

        db.add(brand)

        db.commit()

        db.refresh(brand)

        return brand

    @staticmethod
    def find_by_id(
            db: Session,
            brand_id: str
        ):
    
            brand =  (
                db.query(Brand)
                .filter(Brand.id == brand_id)  
                .first()
            )
            return brand

    @staticmethod
    def find_all(
            db: Session
        ):
    
            brands =  (
                db.query(Brand)
                .all()
            )
            return brands

    @staticmethod
    def update(
            db: Session,
            brand: Brand,
            payload: dict
        ):

            for key, value in payload.items():
                setattr(brand, key, value)

            db.commit()

            db.refresh(brand)

            return brand

    @staticmethod
    def delete(
            db: Session,
            brand: Brand
        ):

            db.delete(brand)

            db.commit()

            return True