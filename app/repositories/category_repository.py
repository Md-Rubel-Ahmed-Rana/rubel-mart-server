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