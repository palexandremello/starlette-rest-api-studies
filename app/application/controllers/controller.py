from abc import ABC, abstractmethod
from app.application.helpers.http import HttpResponse, server_error

class Controller(ABC):
    @abstractmethod
    async def perfom(self, http_request: any) -> HttpResponse:
        pass
    
    async def handle(self, http_request: any)  -> HttpResponse:
      try:
        return await self.perfom(http_request)
      except Exception as error:
        return server_error(error)