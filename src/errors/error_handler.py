from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError

def error_handler(error: Exception) -> HttpRequest:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )