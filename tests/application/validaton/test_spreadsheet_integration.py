from app.application.errors.validation import InvalidSpreadsheetError
from app.application.validation.spreadsheet_integration import SpreadsheetIntegration
from app.application.validation.validator import Validator
import pandas as pd

def make_dataframe():
    return pd.DataFrame([], columns=['column1', 'column2', 'column3'])

def test_SpreadsheetIntegration_should_be_same_instance_of_validator_interface():
    dataframe = make_dataframe()
    sut = SpreadsheetIntegration(dataframe, ['column1'])
    assert isinstance(sut, Validator)

def test_should_be_throw_InvalidSpreadsheetError_when_dataframe_has_invalid_columns():
    dataframe = make_dataframe()
    sut = SpreadsheetIntegration(dataframe, ['column1'])
    error = sut.validate()
    assert isinstance(error, InvalidSpreadsheetError)

def test_should_be_None_when_dataframe_has_valid_columns():
    dataframe = make_dataframe()
    sut = SpreadsheetIntegration(dataframe, ['column1', 'column2', 'column3'])
    error = sut.validate()
    assert error == None