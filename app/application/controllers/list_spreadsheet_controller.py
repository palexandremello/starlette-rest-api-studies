import http
from typing import Type
from app.application.errors.http_errors import HttpErrors
from app.application.helpers.http import HttpRequest, HttpResponse
from app.main.interface.route import RouteInterface
from app.domain.usecases.list_spreadsheet import ListSpreadsheet


class ListSpreadsheetController(RouteInterface):
    def __init__(self, list_spreadsheet_use_case: Type[ListSpreadsheet]) -> None:
        self.list_spreadsheet_use_case = list_spreadsheet_use_case

    async def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.query:
            query_params = http_request.query

            if "initial_date" in query_params and "final_date" in query_params:
                initial_date = query_params['initial_date']
                final_date = query_params['final_date']
                
                response = self.list_spreadsheet_use_case.list_spreadsheets_by_date(initial_date=initial_date, final_date=final_date)
                    
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