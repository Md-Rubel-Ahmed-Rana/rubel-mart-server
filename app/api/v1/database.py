from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import engine

router = APIRouter()


@router.get("/health")
async def database_health():

    try:

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "message": "Database connected successfully",
            "success": True,
            "status_code": 200,
            "data": {}
        }

    except Exception as error:

        return {
            "message": str(error),
            "success": False,
            "status_code": 500,
            "data": {}
        }