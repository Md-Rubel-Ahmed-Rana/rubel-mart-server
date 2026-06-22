from app.repositories.user_repository import UserRepository
from app.utils.response import success_response
from sqlalchemy.orm import Session
from app.utils.password import hash_password
from app.exceptions.api_exception import ApiException


class AuthService:

    @staticmethod
    async def get_profile():

        user = await UserRepository.get_profile()

        return success_response(
            message="Profile retrieved successfully",
            data=user
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
    async def login():

        user = await UserRepository.get_user_by_email()

        return {
            "message": "Login successful",
            "success": True,
            "status_code": 200,
            "data": user
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