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

        query_params = http_request.query
<<<<<<< HEAD

        if "initial_date" in query_params and "final_date" in query_params:
            initial_date = query_params['initial_date']
            final_date = query_params['final_date']   
            response = self.list_spreadsheet_use_case.list_spreadsheets_by_date(initial_date=initial_date, final_date=final_date)
        elif "initial_date"  not in query_params and "final_date" not in query_params:
            response = self.list_spreadsheet_use_case.list_all_spreadsheets()
        else:
            response = {"success": False, "data": None}

=======
        if "initial_date" in query_params and "final_date" in query_params:
            initial_date = query_params['initial_date']
            final_date = query_params['final_date']   
            response = self.list_spreadsheet_use_case.list_spreadsheets_by_date(initial_date=initial_date, final_date=final_date)
        elif "initial_date"  not in query_params and "final_date" not in query_params:
            response = self.list_spreadsheet_use_case.list_all_spreadsheets()
        else:
            response = {"success": False, "data": None}

>>>>>>> 973ce23c1c917dfa6579b184c6b9f02c4acde0be
        if response['success'] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error['status_code'], body=http_error['body']
            )
        return HttpResponse(status_code=200, body=response['data'])