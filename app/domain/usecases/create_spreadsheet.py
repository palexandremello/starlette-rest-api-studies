
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List
from app.domain.entities.spreadsheet import Spreadsheet


class CreateSpreadsheet(ABC):
    """ Interface to CreateSpreadsheet use case"""

    @abstractmethod
    def create(cls,filename: str, initial_date: datetime, final_date: datetime, status_id: int, path: str) -> Dict[bool, List[Spreadsheet]]:
        
        raise Exception("Should implement method: by_spreadsheet_id")


