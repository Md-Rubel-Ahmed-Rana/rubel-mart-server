from app.repositories.user_repository import UserRepository
from app.utils.response import success_response
from sqlalchemy.orm import Session
from app.utils.password import hash_password
from app.exceptions.api_exception import ApiException
from app.core.jwt import jwt_service

from app.utils.password import (
    verify_password
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
    async def refresh_token():

        return {
            "message": "Token refreshed successfully",
            "success": True,
            "status_code": 200,
            "data": {}
        }

    @staticmethod
    async def logout():

        return {
            "message": "Logout successful",
            "success": True,
            "status_code": 200,
            "data": {}
        }