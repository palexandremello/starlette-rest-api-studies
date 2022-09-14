
from typing import List, Type

from app.data.interfaces.file_uploader_interface import FileUploader
from app.domain.entities.file import File
from app.domain.usecases.file_upload import FileUpload as FileUploadInterface


class UploadSpreadsheet(FileUploadInterface):
    def __init__(self, file_uploader: FileUploader) -> None:
        self.file_uploader = file_uploader
    
    async def upload(self, files: List[File]) -> List[str]:
        
        uploaded_files = await self.file_uploader.upload(files)
        
        if not uploaded_files:
            raise Exception("error file")

        
        return uploaded_files