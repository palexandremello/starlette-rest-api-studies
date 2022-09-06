
from app.application.errors.validation import RequiredFieldError
from app.application.validation.required import Required, RequiredBuffer
import io

def make_sut():
    return RequiredBuffer('', 'any_field')


def test_should_be_same_instance():
    sut = make_sut()
    assert isinstance(sut, RequiredBuffer)

def test_should_return_RequiredFieldError_if_value_is_empty():
    invalid_buffer  = io.BytesIO()
    invalid_buffer.write(b'')
    sut = RequiredBuffer(invalid_buffer)
    error = sut.validate()
    assert isinstance(error, RequiredFieldError), f"Expected: {RequiredFieldError}, Result: {error}"

def test_should_return_None_if_value_is_not_empty():
    valid_buffer  = io.BytesIO()
    valid_buffer.write(b'a')
    sut = RequiredBuffer(valid_buffer, 'any_field')
    error = sut.validate()
    assert error == None, f"Expected: {None}, Result: {error}"
