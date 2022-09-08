from abc import ABC, abstractmethod
from typing import Type
from app.application.helpers.http import HttpRequest, HttpResponse


class RouteInterface(ABC):

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise Exception('Should be implement: route')