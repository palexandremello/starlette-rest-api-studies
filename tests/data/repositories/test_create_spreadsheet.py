from typing import List
import pytest
from datetime import datetime
from unittest.mock import MagicMock
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface
from app.data.repositories.create_spreadsheet import CreateSpreadsheet
from app.domain.entities.spreadsheet import Spreadsheet


INITIAL_DATE = datetime(2022, 1, 1, 1)
FINAL_DATE = datetime(2022, 2, 1, 1)

class SpreadsheetRepositoryStub(SpreadsheetRepositoryInterface):
    def insert_spreadsheet(self, filename: str, initial_date: datetime, final_date: datetime) -> Spreadsheet:
        return super().insert_spreadsheet(filename, initial_date, final_date)
    
    def select_spreadsheet(self, spreadsheet_id: int = None) -> List[Spreadsheet]:
        return super().select_spreadsheet(spreadsheet_id)


def mock_spreadsheet_repository():
    spreadsheet_repository = SpreadsheetRepositoryStub()
    spreadsheet_repository.insert_spreadsheet = MagicMock(return_value=Spreadsheet('any_id', 'any_filename', INITIAL_DATE, FINAL_DATE, 'any_link'))
    return spreadsheet_repository

def test_should_be_create_a_spreadsheet_conciliation():
    spreadsheet_repository = mock_spreadsheet_repository()
    attributes = {"id": 'any_id', "filename": 'any_filename', "initial_date":INITIAL_DATE, "final_date": FINAL_DATE, 'link': "any_link"}
    sut = CreateSpreadsheet(spreadsheet_repository)
    response = sut.create(attributes['filename'], attributes['initial_date'], attributes['final_date'])
    assert response['success'] == True
    assert response['data'].to_dict() == attributes


def test_should_not_create_a_spradsheet_when_payload_is_invalid():
    spreadsheet_repository = mock_spreadsheet_repository()
    attributes = {"id": 'any_id', "filename": 'any_filename', "initial_date":INITIAL_DATE, "final_date": FINAL_DATE, 'link': "any_link"}
    sut = CreateSpreadsheet(spreadsheet_repository)
    response = sut.create(attributes['filename'], 'any_date', attributes['final_date'])
    assert response['success'] == False
    assert response['data'] is None