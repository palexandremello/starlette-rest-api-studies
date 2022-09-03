from app.application.controllers.spreadsheet_controller import SpreadsheetController
from app.application.controllers.controller import Controller

def make_sut():
    return SpreadsheetController()

def test_should_be_extend_controller():
    sut = make_sut()
    assert isinstance(sut, Controller)