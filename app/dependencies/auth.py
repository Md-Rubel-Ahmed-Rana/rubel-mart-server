from fastapi import (
    Cookie,
    Request
)

from jwt import (
    ExpiredSignatureError,
    InvalidTokenError
)

from app.core.cookie import (
    ACCESS_TOKEN_COOKIE,
    REFRESH_TOKEN_COOKIE
)

from app.core.jwt import (
    jwt_service
)

from app.exceptions.api_exception import (
    ApiException
)


async def get_current_user(
    request: Request,

    access_token: str | None = Cookie(
        default=None,
        alias=ACCESS_TOKEN_COOKIE
    ),

    refresh_token: str | None = Cookie(
        default=None,
        alias=REFRESH_TOKEN_COOKIE
    )
):

    if not access_token:

        raise ApiException(
            "Unauthenticated access",
            401
        )

    try:

        payload = (
            jwt_service.verify_token(
                access_token
            )
        )

        request.state.user = payload

        return payload

    except ExpiredSignatureError:

        if not refresh_token:

            raise ApiException(
                "Session expired",
                401
            )

        try:

            refresh_payload = (
                jwt_service.verify_token(
                    refresh_token
                )
            )

            request.state.user = (
                refresh_payload
            )

            request.state.rotate_tokens = (
                True
            )

            return refresh_payload

        except Exception:

            raise ApiException(
                "Session expired",
                401
            )

    except InvalidTokenError:

        raise ApiException(
            "Invalid token",
            401
        )