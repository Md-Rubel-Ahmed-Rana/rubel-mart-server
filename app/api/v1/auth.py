from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response
)
from app.utils.response import (
    success_response
)
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth_schema import (
    LoginSchema
)
from app.schemas.user_schema import (
    RegisterSchema
)
from app.services.auth_service import (
    AuthService
)
from app.dependencies.auth import (
    get_current_user
)

router = APIRouter()

@router.get("/")
async def profile(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    
    print("Auth user", current_user)
    print("Auth user id", current_user["id"])
    
    result = await AuthService.get_profile(
        db,
        current_user["id"]
    )

    return  result
 
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
    

@router.post("/login")
async def login(
    payload: LoginSchema,
    response: Response,
    db: Session = Depends(get_db)
):

    result = await AuthService.login(
        db,
        payload.email,
        payload.password
    )

    response.set_cookie(
        key="rubel_mart_access_token",
        value=result["access_token"],
        httponly=True,
        secure=True,
        samesite="none",
        max_age=60 * 60 * 24  # 1 day
    )

    response.set_cookie(
        key="rubel_mart_refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="none",
        max_age=60 * 60 * 24 * 7  # 7 days
    )

    return success_response(
        message="Login successful",
        data={
            "user": {
                "id": result["user"].id,
                "email": result["user"].email,
                "first_name": result["user"].first_name,
                "last_name": result["user"].last_name
            }
        }
    )