from app.repositories.auth_repository import AuthRepository
from app.utils.response import success_response


class AuthService:

    @staticmethod
    async def get_profile():

        user = await AuthRepository.get_profile()

        return success_response(
            message="Profile retrieved successfully",
            data=user
        )      
    
    @staticmethod
    async def register():

        user = await AuthRepository.create_user()

        return {
            "message": "User registered successfully",
            "success": True,
            "status_code": 201,
            "data": user
        }

    @staticmethod
    async def login():

        user = await AuthRepository.get_user_by_email()

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