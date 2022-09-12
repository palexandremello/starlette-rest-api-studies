from datetime import datetime
from typing import List
from unittest.mock import MagicMock
from app.application.controllers.create_spreadsheet_controller import CreateSpreadsheetController
from app.application.helpers.http import HttpRequest
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface
from app.data.repositories.create_spreadsheet import CreateSpreadsheet
from app.domain.entities.spreadsheet import Spreadsheet
from app.main.interface.route import RouteInterface


INITIAL_DATE = datetime(2022, 1, 1, 1)
FINAL_DATE = datetime(2022, 2, 1, 1)


class SpreadsheetRepositoryStub(SpreadsheetRepositoryInterface):
    async def insert_spreadsheet(self, filename: str, initial_date: datetime, final_date: datetime) -> Spreadsheet:
        return await super().insert_spreadsheet(filename, initial_date, final_date)
    
    async def select_spreadsheet(self, spreadsheet_id: int = None) -> List[Spreadsheet]:
        return await super().select_spreadsheet(spreadsheet_id)

def mock_spreadsheet_repository():
    spreadsheet_repository = SpreadsheetRepositoryStub()
    spreadsheet_repository.insert_spreadsheet = MagicMock(return_value=Spreadsheet('any_id', 'any_filename', INITIAL_DATE, FINAL_DATE, 'any_link'))
    return spreadsheet_repository



def test_should_be_same_instance_of_RouteInterface():
    sut = CreateSpreadsheetController('any_usecase')

    assert isinstance(sut, RouteInterface)



def test_should_return_a_response_when_route_is_success():
    attributes = {"filename": 'any_filename', "initial_date":INITIAL_DATE, "final_date": FINAL_DATE}
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest(body=attributes)

    response = sut.route(request)
    
    assert response.status_code == 200

def test_should_return_error_when_request_is_empty():
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest()

    response = sut.route(request)
    assert response.status_code == 400
    assert "error" in response.body


def test_should_return_error_when_request_wrong_body():
    attributes = { "filename": 'any_filename', "initial_date":INITIAL_DATE}
    spreadsheet_repository = mock_spreadsheet_repository()
    create_spreadsheet_use_case = CreateSpreadsheet(spreadsheet_repository)
    sut = CreateSpreadsheetController(create_spreadsheet_use_case)
    request = HttpRequest(body=attributes)

    response = sut.route(request)

    assert response.status_code == 422
    assert "error" in response.body