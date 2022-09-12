from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from app.domain.entities.spreadsheet import Spreadsheet


class SpreadsheetRepositoryInterface(ABC):
    """ Interface to SpreadsheetRepository """

    @abstractmethod
    def insert_spreadsheet(self, filename: str, initial_date: datetime, final_date: datetime) -> Spreadsheet:
        
        raise Exception("Method not implemented")

    
    @abstractmethod
    def select_spreadsheet(self, spreadsheet_id: int = None) -> List[Spreadsheet]:
        raise Exception("method not implemented")

    @abstractmethod
    def list_spreadsheet(self, initial_date: datetime, final_date: datetime) -> List[Spreadsheet]:
        raise Exception("method not implemented")