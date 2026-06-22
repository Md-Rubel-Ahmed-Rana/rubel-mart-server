from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.user_schema import (
    RegisterSchema
)

from app.services.auth_service import (
    AuthService
)

router = APIRouter()


@router.post("/register")
async def register(
    payload: RegisterSchema,
    db: Session = Depends(get_db)
):

    try:

        user = AuthService.register(
            db,
            payload
        )

        return {
            "message": "User registered successfully",
            "success": True,
            "status_code": 201,
            "data": {
                "id": user.id,
                "email": user.email
            }
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )