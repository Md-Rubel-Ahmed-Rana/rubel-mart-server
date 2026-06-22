from sqlalchemy.orm import Session
from app.exceptions.api_exception import ApiException
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
        print("user from repo", user)
        return user