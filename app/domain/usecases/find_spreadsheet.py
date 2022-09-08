
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List
from app.domain.entities.spreadsheet import Spreadsheet


class FindSpreadsheet(ABC):
    """ Interface to FindSpreadsheet use case"""

    @abstractmethod
    def by_spreadsheet_id(cls, spreadsheet_id: int) -> Dict[bool, List[Spreadsheet]]:
        
        raise NotImplemented("Should implement method: by_spreadsheet_id")


    @abstractmethod
    def by_date_id(cls, initial_date: datetime, final_date: datetime) -> Dict[bool, List[Spreadsheet]]:
        
        raise NotImplemented("Should implement method: by_date_id")