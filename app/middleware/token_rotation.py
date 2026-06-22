from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from app.core.jwt import (
    jwt_service
)

from app.core.cookie import (
    ACCESS_TOKEN_COOKIE,
    REFRESH_TOKEN_COOKIE
)


class TokenRotationMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        response = await call_next(
            request
        )

        if getattr(
            request.state,
            "rotate_tokens",
            False
        ):

            payload = request.state.user

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

            response.set_cookie(
                key=ACCESS_TOKEN_COOKIE,
                value=access_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=86400
            )

            response.set_cookie(
                key=REFRESH_TOKEN_COOKIE,
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite="none",
                max_age=604800
            )

        return response