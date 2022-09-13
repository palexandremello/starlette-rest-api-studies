from typing import Type
import traceback
from starlette.requests import Request
from app.application.helpers.http import HttpRequest, HttpResponse
from app.main.interface.route import RouteInterface as Route
from app.application.errors.http_errors import HttpErrors
from sqlalchemy.exc import IntegrityError

async def starlette_adapter(request: Request, api_route: Type[Route]) -> any:
    """Adapter pattern to Starlette
    :param - Starlette Request
    :api_route: Composite Routes
    """
    try:
        query_string_params = dict(request.query_params)
        form = await request.form()
    except Exception as error:
        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error['status_code'], body=http_error['body'])
    

    http_request = HttpRequest(header=request.headers, body=request.json, form=form, query=query_string_params)



    try:
        response = await api_route.route(http_request)
    except IntegrityError:
        print("aqui aqui entao?")
        http_error = HttpErrors.error_409()

        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error['body']
        )
    
    except Exception as exc:
        print(traceback.format_exc())
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"]
        )

    
    return response