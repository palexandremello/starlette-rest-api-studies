from typing import List
from unittest.mock import AsyncMock, MagicMock
from app.domain.usecases.file_upload import FileUpload as FileUploadInterface
from app.domain.entities.file import File
from app.data.repositories.upload_spreadsheet import UploadSpreadsheet


class FileUploaderStub(FileUploadInterface):
    async def upload(self, files: List[File]) -> List[str]:
        return await super().upload(files)


def mock_file_uploader():
    file_uploader = FileUploaderStub()
    file_uploader.upload = AsyncMock(return_value='any_uploaded_file')
    return file_uploader

async def test_should_be_upload_spreadsheet_file():
    file_uploader = mock_file_uploader()
    sut = UploadSpreadsheet(file_uploader)
    file_uploaded_path =  await sut.upload('any_uploaded_file')

    assert file_uploaded_path == 'any_uploaded_file'


async def test_should_be_throws_when_upload_spreadsheet_fails():
    file_uploader = mock_file_uploader()
    file_uploader.upload = AsyncMock(return_value=[])
    sut = UploadSpreadsheet(file_uploader)
    error = await sut.upload('any_file')
    assert isinstance(error, Exception)

