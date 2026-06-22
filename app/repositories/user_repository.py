from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:

    @staticmethod
    def find_by_email(
        db: Session,
        email: str
    ):

        user =  (
            db.query(User)
            .filter(User.email == email)
            .first()
        )
        return user

    @staticmethod
    def create_user(
        db: Session,
        payload: dict
    ):

        user = User(**payload)

        db.add(user)

        db.commit()

        db.refresh(user)

        return user
    
    @staticmethod
    def find_by_id(db: Session, id: str):
        
        user = (
           db.query(User).filter(User.id == id)
           .first()
        )
        return user
    
    @staticmethod
    def update_by_id(
        db: Session,
        user: User,
        payload: dict
    ):
        for key, value in payload.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def update_image(
        db: Session,
        user: User,
        image_id: str
    ):
        user.image_id = image_id

        db.commit()

        db.refresh(user)

        return user