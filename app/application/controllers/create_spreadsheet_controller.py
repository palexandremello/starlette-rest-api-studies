from typing import Type
from app.application.errors.http_errors import HttpErrors
from app.application.helpers.http import HttpRequest, HttpResponse
from app.infra.errors.file_upload_errors import FileUploadErrors
from app.main.interface.route import RouteInterface
from app.domain.usecases.create_spreadsheet import CreateSpreadsheet
from app.domain.entities.status import Status
from app.main.interface.service import ServiceInterface
from app.main.composite.file_upload_service_composite import file_upload_service_composer

class CreateSpreadsheetController(RouteInterface):
    def __init__(self, create_spreadsheet_use_case: Type[CreateSpreadsheet]) -> None:
        self.create_spreadsheet_use_case = create_spreadsheet_use_case
        self.file_upload_service: Type[ServiceInterface] = file_upload_service_composer()

    async def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        response = None

        if http_request.form:
            body = http_request.form
            body_params = body.keys()

            if "initial_date" in body_params and "final_date" in body_params:

                status = Status.NOVO.value

                list_of_key = await self.file_upload_service.perfom([body])

                if isinstance(list_of_key, Exception):
                    file_upload_error = FileUploadErrors.invalid_spreadsheet()
                    return HttpResponse(status_code=file_upload_error['status_code'], body=file_upload_error['body'])

                response = self.create_spreadsheet_use_case.create(initial_date=body['initial_date'],
                                                                   final_date=body['final_date'],
                                                                   filename=body['filename'],
                                                                   status=status,
                                                                   path=list_of_key[0])
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