from datetime import datetime, timedelta, timezone
import jwt
from jwt import ExpiredSignatureError

from app.core.config import settings


class JWTService:

    @staticmethod
    def generate_access_token(payload: dict):

        expire = datetime.now(
            timezone.utc
        ) + timedelta(days=1)

        payload.update({
            "exp": expire
        })

        return jwt.encode(
            payload,
            settings.JWT_SECRET,
            algorithm="HS256"
        )
    
    @staticmethod
    def generate_refresh_token(payload: dict):

        expire = datetime.now(
            timezone.utc
        ) + timedelta(days=7)

        payload.update({
            "exp": expire
        })

        return jwt.encode(
            payload,
            settings.JWT_SECRET,
            algorithm="HS256"
        )

    @staticmethod
    def verify_token(token: str):

        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=["HS256"]
        )


jwt_service = JWTService()