from abc import ABC, abstractmethod
from typing import List

class ServiceInterface(ABC):
    @abstractmethod
    async def perfom(self, files: dict) -> List[str] or Exception:
        raise Exception("should implement perfom method")