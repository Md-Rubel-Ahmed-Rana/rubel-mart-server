from fastapi.exceptions import (
    RequestValidationError
)

from app.exceptions.api_exception import (
    ApiException
)

from app.exceptions.handlers import (
    api_exception_handler,
    validation_exception_handler
)


def register_exception_handlers(
    app
):

    app.add_exception_handler(
        ApiException,
        api_exception_handler
    )

    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler
    )