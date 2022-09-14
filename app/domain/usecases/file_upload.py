from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.file import File

class FileUpload(ABC):
    """ Interface to FileUpload use case"""

    @abstractmethod
    async def upload(cls, files: List[File]) -> List[str]:
        raise Exception("should implement upload method")