from typing import Type
from app.application.errors.http_errors import HttpErrors
from app.application.helpers.http import HttpRequest, HttpResponse
from app.main.interface.route import RouteInterface
from app.domain.usecases.create_spreadsheet import CreateSpreadsheet


class CreateSpreadsheetController(RouteInterface):
    def __init__(self, create_spreadsheet_use_case: Type[CreateSpreadsheet]) -> None:
        self.create_spreadsheet_use_case = create_spreadsheet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None
        if http_request.body:
            
            body_params = http_request.body.keys()

            if "initial_date" in body_params and "final_date" in body_params:
                initial_date = http_request.body['initial_date']
                final_date = http_request.body['final_date']
                filename = http_request.body['filename']
                response = self.create_spreadsheet_use_case.create(initial_date=initial_date, final_date=final_date,filename=filename)
            
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