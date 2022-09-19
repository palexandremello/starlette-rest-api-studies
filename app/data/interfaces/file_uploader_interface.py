from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.file import File


class FileUploader(ABC):
    """ Interface to FileUploader """

    @abstractmethod
    async def upload(self, files: List[File] or File) -> List[str] or Exception:
        raise Exception("not implemented upload method")