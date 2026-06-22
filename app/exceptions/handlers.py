from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions.api_exception import ApiException
from app.utils.response import error_response


async def api_exception_handler(
    request: Request,
    exc: ApiException
):

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(
            message=exc.message,
            status_code=exc.status_code
        )
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    errors = []

    for error in exc.errors():

        field = error["loc"][-1]

        message = error["msg"]

        if message == "Field required":
            message = (
                f"{field.replace('_', ' ').title()} "
                f"is required"
            )

        errors.append({
            "field": field,
            "message": message
        })

    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation failed",
            "success": False,
            "status_code": 422,
            "data": {
                "errors": errors
            }
        }
    )