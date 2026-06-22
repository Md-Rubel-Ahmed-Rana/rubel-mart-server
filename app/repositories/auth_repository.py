class AuthRepository:

    @staticmethod
    async def get_profile():
        return {
            "id": 1,
            "name": "Rubel Ahmed Rana",
            "email": "rana@example.com",
            "image": "https://images.com/profiles/mdrubelahmedarna.png"
        }
    
    @staticmethod
    async def create_user():
        return {
            "id": 1,
            "name": "Rubel Ahmed Rana",
            "email": "rana@example.com"
        }

    @staticmethod
    async def get_user_by_email():
        return {
            "id": 1,
            "email": "rana@example.com"
        }