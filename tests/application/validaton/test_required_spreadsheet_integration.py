
from app.application.errors.validation import RequiredFieldError
from app.application.validation.required import RequiredSpreadsheetIntegration
import pandas as pd


def make_sut():
    return RequiredSpreadsheetIntegration('any_dataframe', 'any_field')

def test_should_be_same_instance():
    sut = make_sut()
    assert isinstance(sut, RequiredSpreadsheetIntegration)

def test_should_return_RequiredFieldError_if_value_is_empty():
    sut = RequiredSpreadsheetIntegration('')
    error = sut.validate()
    assert isinstance(error, RequiredFieldError), f"Expected: {RequiredFieldError}, Result: {error}"

def test_should_return_None_if_value_is_not_empty():
    sut = RequiredSpreadsheetIntegration('any_dataframe', 'any_field')
    error = sut.validate()
    assert error == None, f"Expected: {None}, Result: {error}"
