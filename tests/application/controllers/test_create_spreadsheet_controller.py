from datetime import datetime
from typing import List
from unittest import mock
from unittest.mock import MagicMock
from starlette.requests import Request
from app.application.controllers.create_spreadsheet_controller import CreateSpreadsheetController
from app.application.helpers.http import HttpRequest
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface
from app.data.repositories.create_spreadsheet import CreateSpreadsheet
from app.domain.entities.spreadsheet import Spreadsheet
from app.main.interface.route import RouteInterface
from starlette.requests import Request
from starlette.datastructures import Headers

def build_request(
    method: str = "GET",
    server: str = "www.example.com",
    path: str = "/",
    headers: dict = None,
    body: str = None,
    form: str = None,
) -> Request:
    if headers is None:
        headers = {}
    request = Request(
        {
            "type": "http",
            "path": path,
            "headers": Headers(headers).raw,
            "http_version": "1.1",
            "method": method,
            "scheme": "https",
            "client": ("127.0.0.1", 8080),
            "server": (server, 443),
        }
    )
    if body:

        async def request_body():
            return body

        request.body = request_body
    
    if form:
        async def request_form():
            return form
        request.form = request_form
    return request


INITIAL_DATE = datetime(2022, 1, 1, 1)
FINAL_DATE = datetime(2022, 2, 1, 1)


class SpreadsheetRepositoryStub(SpreadsheetRepositoryInterface):
    async def insert_spreadsheet(self, filename: str, initial_date: datetime, final_date: datetime) -> Spreadsheet:
        return await super().insert_spreadsheet(filename, initial_date, final_date)
    
    async def select_spreadsheet(self, spreadsheet_id: int = None) -> List[Spreadsheet]:
        return await super().select_spreadsheet(spreadsheet_id)
    
    async def list_spreadsheet(self, initial_date: datetime, final_date: datetime) -> List[Spreadsheet]:
        return await super().list_spreadsheet(initial_date, final_date)

def mock_spreadsheet_repository():
    spreadsheet_repository = SpreadsheetRepositoryStub()
    spreadsheet_repository.insert_spreadsheet = MagicMock(return_value=Spreadsheet('any_id', 'any_filename', INITIAL_DATE, FINAL_DATE, 1, 'any_link'))
    return spreadsheet_repository



def test_should_be_same_instance_of_RouteInterface():
    sut = CreateSpreadsheetController('any_usecase')

    assert isinstance(sut, RouteInterface)



async def test_should_return_a_response_when_route_is_success(valid_buffer, valid_uploadFile):
    file = await valid_uploadFile.read()
    attributes = {"file": valid_uploadFile,
                  "initial_date": '2020-01-01',
                  "final_date": '2020-01-01',
                  "filename": valid_uploadFile.filename,
                  'size': len(file),
                  "content_type": valid_uploadFile.content_type}

    form = build_request(form=attributes)
    form_data = await form.form()
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest(form=form_data)
    response = await sut.route(request)
    
    assert response.status_code == 200


async def test_should_return_a_file_upload_error_when_file_is_invalid(valid_buffer, valid_uploadFile):
    file = await valid_uploadFile.read()
    attributes = {"file": valid_uploadFile,
                  "initial_date": '2020-01-01',
                  "final_date": '2020-01-01',
                  "filename": valid_uploadFile.filename,
                  'size': len(file),
                  "content_type": valid_uploadFile.content_type}

    form = build_request(form=attributes)
    form_data = await form.form()
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest(form=form_data)
    with mock.patch("aioboto3.s3.inject.upload_fileobj", side_effect=Exception("any_error")):
        response = await sut.route(request)
        assert response.status_code == 500
        assert response.body == {'error': 'Invalid spreadsheet file'}

async def test_should_return_error_when_request_is_empty():
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest()

    response = await sut.route(request)
    assert response.status_code == 400
    assert "error" in response.body


async def test_should_return_error_when_request_wrong_body():
    attributes = { "filename": 'any_filename', "initial_date":'2022-01-01'}
    form = build_request(form=attributes)
    form_data = await form.form()
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest(form=form_data)

    response = await sut.route(request)

    assert response.status_code == 422
    assert "error" in response.body