
import io
from app.application.errors.validation import MaxFileSizeError
from app.application.validation.max_file_size import MaxFileSize


MAX_SIZE = 5
def make_buffer(size_of_buffer):
    invalid_buffer  = io.BytesIO()
    for i in range(size_of_buffer * 1024 * 1024):
        _ = invalid_buffer.write(b'a')
    return invalid_buffer

def test_should_be_return_MaxFileSizeError_if_value_is_invalid():
    size_of_buffer = 6
    invalid_buffer = make_buffer(size_of_buffer)
    sut = MaxFileSize(MAX_SIZE, invalid_buffer)
    error = sut.validate()
    assert isinstance(error, MaxFileSizeError)

def test_should_be_return_None_value_is_valid():
    size_of_buffer = 4
    valid_buffer = make_buffer(size_of_buffer)
    sut = MaxFileSize(MAX_SIZE, valid_buffer)
    error = sut.validate()
    assert error == None