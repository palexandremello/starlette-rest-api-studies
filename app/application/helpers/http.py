from typing import TypedDict
from app.application.errors.http import ServerError

class HttpResponse(TypedDict):
    status_code: int
    data: dict

def ok(data: dict) -> HttpResponse:
    return {
        "status_code": 200,
        "data": data
    }

def server_error(error: Exception) -> HttpResponse:
    return {
        "status_code": 500,
         'data': ServerError(error)
    }