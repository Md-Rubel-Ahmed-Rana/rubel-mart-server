from app.repositories.user_repository import UserRepository
from app.utils.response import success_response
from sqlalchemy.orm import Session
from app.exceptions.api_exception import ApiException
from app.core.jwt import jwt_service
from app.schemas.user_schema import  (
    UpdateUserSchema
)
from app.utils.password import (
    verify_password,
    hash_password
)

from app.services.media_service import (
    MediaService
)


class AuthService:

    @staticmethod
    async def get_profile(db: Session, id: str):

        user = (
            UserRepository.find_by_id(db, id)
        )

        return success_response(
            message="Profile retrieved successfully",
            data={
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "image": user.image,
                "role": user.role,
                "status": user.status,
                "is_verified": user.is_verified,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        )      
    
    @staticmethod
    def register(
        db: Session,
        payload
    ):

        existing_user = (
            UserRepository.find_by_email(
                db,
                payload.email
            )
        )

        if existing_user:

            raise ApiException(
                message="Account already exists with this email. Please login or create another account.",
                status_code=409
            )
        
        user_data = {
            "first_name": payload.first_name,
            "last_name": payload.last_name,
            "email": payload.email,
            "password": hash_password(
                payload.password
            )
        }

        return UserRepository.create_user(
            db,
            user_data
        )

    @staticmethod
    async def login(
        db: Session,
        email: str,
        password: str
    ):

        user = (
             UserRepository
            .find_by_email(
                db,
                email
            )
        )

        if not user:

            raise ApiException(
                message="User not found",
                status_code=404
            )

        if not verify_password(
            password,
            user.password
        ):

            raise ApiException(
                message="Invalid email or password",
                status_code=401
            )

        payload = {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }

        access_token = (
            jwt_service
            .generate_access_token(
                payload.copy()
            )
        )

        refresh_token = (
            jwt_service
            .generate_refresh_token(
                payload.copy()
            )
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user
        }

    @staticmethod
    async def forgot_password():

        return {
            "message": "Password reset link sent successfully",
            "success": True,
            "status_code": 200,
            "data": {}
        }
    
    @staticmethod
    async def update_profile(
        db: Session,
        id: str,
        payload: UpdateUserSchema
    ):
        user = UserRepository.find_by_id(
            db,
            id
        )

        if not user:
            raise ApiException(
                "User not found",
                404
            )

        update_data = payload.model_dump(
            exclude_unset=True
        )

        if "password" in update_data and update_data["password"]:

            is_same_password = verify_password(
                update_data["password"],
                user.password
            )

            if is_same_password:
                raise ApiException(
                    "Same password couldn't be changed. Please choose a different password",
                    400
                )

            update_data["password"] = hash_password(
                update_data["password"]
            )

        updated_user = (
            UserRepository.update_by_id(
                db,
                user,
                update_data
            )
        )

        return updated_user
    
    @staticmethod
    async def update_profile_image(
        db,
        user_id: str,
        file
    ):

        user = UserRepository.find_by_id(
            db,
            user_id
        )

        if not user:

            raise ApiException(
                message="User not found",
                status_code=404
            )

        media = await MediaService.upload_file(
            db=db,
            file=file,
            uploaded_by=user.id,
            folder="users"
        )

        user = UserRepository.update_image(
            db,
            user,
            media.id
        )

        return user


