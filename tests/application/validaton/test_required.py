
from app.application.errors.validation import RequiredFieldError
from app.application.validation.required import Required
from app.application.validation.validator import Validator


def make_sut():
    return Required(None, 'any_field')


def test_should_be_same_instance():
    sut = make_sut()
    assert isinstance(sut, Validator)

def test_should_return_RequiredFieldError_if_value_is_none():
    sut = Required(None, 'any_field')
    error = sut.validate()
    assert isinstance(error, RequiredFieldError)

def test_should_return_None_if_value_is_not_empty():
    sut = Required('any_value', 'any_field')
    error = sut.validate()
    assert error == None, "Expected: {None}, Result: {error}"