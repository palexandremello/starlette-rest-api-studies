from typing import Type
from app.application.errors.http_errors import HttpErrors
from app.application.helpers.http import HttpRequest, HttpResponse
from app.main.interface.route import RouteInterface
from app.domain.usecases.create_spreadsheet import CreateSpreadsheet
from app.domain.entities.status import Status

class CreateSpreadsheetController(RouteInterface):
    def __init__(self, create_spreadsheet_use_case: Type[CreateSpreadsheet]) -> None:
        self.create_spreadsheet_use_case = create_spreadsheet_use_case

    async def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.form:
            body = await http_request.form()
            body_params = body.keys()

            if "initial_date" in body_params and "final_date" in body_params:
                initial_date = body['initial_date']
                final_date = body['final_date']
                filename = body['filename']
                status = Status.NOVO.value
                response = self.create_spreadsheet_use_case.create(initial_date=initial_date, final_date=final_date,
                                                                  filename=filename,status=status)
            else:
                response = {"success": False, "data": None}
            
            if response['success'] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error['status_code'], body=http_error['body']
                )
            
            return HttpResponse(status_code=200, body=response['data'])
        

        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error['status_code'], body=http_error['body'])