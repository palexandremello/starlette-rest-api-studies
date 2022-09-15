import pytest
import boto3
from unittest import mock
from app.data.interfaces.file_uploader_interface import FileUploader
from app.domain.entities.file import File
from app.infra.gateways.aws_s3_file_upload import AwsS3FileUpload

BUCKET = 'any_bucket'



def test_should_be_able_to_instantiate_AwsS3FileUpload_same_interface_as_FileUploader():
    sut = AwsS3FileUpload(BUCKET)

    assert isinstance(sut, FileUploader)

@pytest.mark.asyncio
async def test_should_be_able_throw_exception_if_buffer_is_invalid():
    sut = AwsS3FileUpload(BUCKET)
    file = File('planilha.xlsx', 100, 'spreadsheet', 'xlsx', 1)
    with mock.patch("aioboto3.s3.inject.upload_fileobj", side_effect=Exception("any_error")):
        error = await sut.upload([file])
        assert isinstance(error, Exception)


@pytest.mark.asyncio
@mock.patch("aioboto3.s3.inject.upload_fileobj")
async def test_should_be_able_to_upload_a_file(mock_object_upload_fileobj, valid_buffer):
    mock_object_upload_fileobj.return_value = mock.Mock(return_value="any_response")
    sut = AwsS3FileUpload(BUCKET)
    file = File('planilha.xlsx', len(valid_buffer.getvalue()), 'spreadsheet', 'xlsx', valid_buffer.getvalue() )
    list_of_key = await sut.upload([file])
    
    assert list_of_key == ['input_spreadsheets/planilha.xlsx']
