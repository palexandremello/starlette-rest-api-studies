import pytest
from app.application.validation.composite import ValidationComposite
from app.application.validation.validator import Validator
from unittest.mock import MagicMock

class ValidatorStub(Validator):
    def validate(self) -> Exception or None:
        return super().validate()

def make_validators_mock(value_one, value_two):
    validator1 = ValidatorStub()
    validator1.validate = MagicMock(return_value=value_one)
    validator2 = ValidatorStub()
    validator2.validate = MagicMock(return_value=value_two)
    return [validator1, validator2]

def test_should_return_None_if_all_Validators_return_None(mocker):
    sut = ValidationComposite(make_validators_mock(None, None))
    error = sut.validate()
    print(error)
    assert error == None

def test_should_return_a_error_if_any_Validator_fails():
    sut = ValidationComposite(make_validators_mock(Exception('error_1'), None))
    error= sut.validate()    
    assert isinstance(error, Exception)
