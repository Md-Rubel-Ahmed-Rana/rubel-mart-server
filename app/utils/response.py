def success_response(
    message: str,
    data: dict = {},
    status_code: int = 200
):
    return {
        "message": message,
        "success": True,
        "status_code": status_code,
        "data": data
    }


def error_response(
    message: str,
    status_code: int = 400
):
    return {
        "message": message,
        "success": False,
        "status_code": status_code,
        "data": {}
    }