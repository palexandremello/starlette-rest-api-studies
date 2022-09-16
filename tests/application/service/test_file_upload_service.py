import pytest
from typing import List
from unittest.mock import AsyncMock, MagicMock
from app.application.services.file_upload_service import FileUploadService
from app.domain.entities.file import File
from app.data.repositories.upload_spreadsheet import UploadSpreadsheet
from app.main.interface.service import ServiceInterface
from app.data.interfaces.file_uploader_interface import FileUploader

class FileUploaderStub(FileUploader):
   async def upload(self, files: List[File] or File) -> List[str] or Exception:
        return files

def mock_file_uploader():
    file_uploader = FileUploaderStub()
    file_uploader.upload = AsyncMock(return_value=['any_key_uploaded'])
    return file_uploader

def mock_exception_file_uploader():
    file_uploader = FileUploaderStub()
    file_uploader.upload = AsyncMock(return_value=None)
    return file_uploader

def test_should_be_same_instance_of_service_interface():
    file_uploader = mock_file_uploader()
    upload_spreadsheet_use_case = UploadSpreadsheet(file_uploader)
    sut = FileUploadService(upload_spreadsheet_use_case)

    assert isinstance(sut, ServiceInterface)

@pytest.mark.asyncio
async def test_should_perfom_a_upload_file(valid_buffer):
    file_uploader = mock_file_uploader()
    upload_spreadsheet_use_case = UploadSpreadsheet(file_uploader)
    sut = FileUploadService(upload_spreadsheet_use_case)

    list_of_key = await sut.perfom([{'file': valid_buffer, 'filename': 'teste.xlsx'}])
    assert list_of_key == ['any_key_uploaded']


@pytest.mark.asyncio
async def test_should_return_exception_if_perfom_fails(valid_buffer):
    file_uploader = mock_exception_file_uploader()
    upload_spreadsheet_use_case = UploadSpreadsheet(file_uploader)
    sut = FileUploadService(upload_spreadsheet_use_case)

    error = await sut.perfom([{'file': valid_buffer, 'filename': 'teste.xlsx'}])
    assert isinstance(error, Exception)