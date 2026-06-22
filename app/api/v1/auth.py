from fastapi import APIRouter

from app.services.auth_service import AuthService

router = APIRouter()


@router.get("/")
async def get_profile():
    return await AuthService.get_profile()

@router.post("/register")
async def register():
    return await AuthService.register()


@router.post("/login")
async def login():
    return await AuthService.login()


@router.post("/forgot-password")
async def forgot_password():
    return await AuthService.forgot_password()


@router.post("/refresh-token")
async def refresh_token():
    return await AuthService.refresh_token()


@router.post("/logout")
async def logout():
    return await AuthService.logout()