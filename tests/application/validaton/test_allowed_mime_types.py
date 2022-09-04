from app.application.errors.validation import InvalidMimeTypeError
from app.application.validation.allowed_mime_types import AllowedMimeTypes


def test_should_return_InvmalidMimeTypeError_if_value_is_invalid():
    sut = AllowedMimeTypes('csv', 'application/vnd.ms-excel')
    error = sut.validate()
    assert isinstance(error, InvalidMimeTypeError)

def test_should_return_None_if_value_is_valid():
    sut = AllowedMimeTypes('xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    error = sut.validate()
    assert error == None

def test_should_return_None_if_value_is_valid():
    sut = AllowedMimeTypes('xls', 'application/vnd.ms-excel')
    error = sut.validate()
    assert error == None