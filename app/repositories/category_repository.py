from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.media import Media


class CategoryRepository:

    @staticmethod
    def find_by_name(
            db: Session,
            name: str
        ):
    
            category =  (
                db.query(Category)
                .filter(Category.name == name)  
                .first()
            )
            return category


    
    @staticmethod
    def create(
        db: Session,
        payload: dict
    ):

        category = Category(**payload)

        db.add(category)

        db.commit()

        db.refresh(category)

        return category

    @staticmethod
    def find_by_id(
            db: Session,
            category_id: str
        ):
    
            category =  (
                db.query(Category)
                .filter(Category.id == category_id)  
                .first()
            )
            return category

    @staticmethod
    def find_all(
            db: Session
        ):
    
            categories =  (
                db.query(Category)
                .all()
            )
            return categories

    @staticmethod
    def update(
            db: Session,
            category: Category,
            payload: dict
        ):

            for key, value in payload.items():
                setattr(category, key, value)

            db.commit()

            db.refresh(category)

            return category

    @staticmethod
    def delete(
            db: Session,
            category: Category
        ):

            db.delete(category)

            db.commit()

            return True