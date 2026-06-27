from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    UploadFile,
    File
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
    RegisterSchema,
    UpdateUserSchema
)
from app.services.auth_service import (
    AuthService
)
from app.dependencies.auth import (
    get_current_user
)

router = APIRouter()

@router.post("/register")
async def register(
    payload: RegisterSchema,
    db: Session = Depends(get_db)
):

    try:

        user = await AuthService.register(
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
    



@router.get("/")
async def profile(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):  
    result = await AuthService.get_profile(
        db,
        current_user["id"]
    )

    return  result

@router.patch("/image")
async def update_profile_image(
    file: UploadFile = File(...),
    db: Session = Depends(
        get_db
    ),
    current_user=Depends(
        get_current_user
    )
):
    
    user = await AuthService.update_profile_image(
        db=db,
        user_id=current_user["id"],
        file=file
    )

    return success_response(
        message="Profile image updated successfully",
        data={
            "id": user.id,
            "image": (
                user.image.url
                if user.image
                else None
            )
        }
    )

@router.patch("/")
async def update_profile(
    payload: UpdateUserSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    user = await AuthService.update_profile(
        db,
        current_user["id"],
        payload
    )

    return {
        "success": True,
        "message": "Profile updated successfully",
        "data": {
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
    }
 
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
    max_age=60 * 60 * 24,
    path="/",
    )

    response.set_cookie(
        key="rubel_mart_refresh_token",
        value=result["refresh_token"],
        httponly=True,
        secure=True,
        samesite="none",
        max_age=60 * 60 * 24 * 7,
        path="/",
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