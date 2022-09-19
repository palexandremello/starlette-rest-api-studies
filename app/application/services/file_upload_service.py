from typing import List, Type
from app.domain.entities.file import File
from app.domain.usecases.file_upload import FileUpload
from app.main.interface.service import ServiceInterface

class FileUploadService(ServiceInterface):

    def __init__(self, upload_file_use_case: Type[FileUpload]) -> None:
        self.upload_file_use_case = upload_file_use_case
        self.files = []

    async def perfom(self, files: dict) -> List[str] or Exception:
        for file in files:
            file_model = File(file['filename'], file['size'], 'xlsx', 'xlsx', file['file'] )
            print(file_model)
            self.files.append(file_model)

        list_of_key =  await self.upload_file_use_case.upload(self.files)

        return list_of_key