import aioboto3
from typing import List
from app.data.interfaces.file_uploader_interface import FileUploader
from app.domain.entities.file import File


class AwsS3FileUpload(FileUploader):
    def __init__(self, bucket: str) -> None:
        self.session = self.get_session()
        self.__service = "s3"
        self.__path = "input_spreadsheets"
        self.__bucket = bucket
        self.__list_of_keys = []
    
    def get_session(self):
        return aioboto3.Session()

    async def upload(self, files: List[File] or File) -> List[str] or Exception:
        async with self.session.client(self.__service) as s3:
            try:
                for file in files:
                    key = f"{self.__path}/{file.filename}"
                    self.__list_of_keys.append(key)
                    await s3.upload_fileobj(file.content, self.__bucket, key)
            except Exception as error:
                return error
        
        return self.__list_of_keys