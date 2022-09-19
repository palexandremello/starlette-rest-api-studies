
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List
from app.domain.entities.spreadsheet import Spreadsheet


class ListSpreadsheet(ABC):
    """ Interface to ListSpreadsheet use case"""
    
    @abstractmethod
    def list_spreadsheets_by_date(cls, initial_date: datetime, final_date: datetime) -> Dict[bool, List[Spreadsheet]]:
        raise NotImplemented("Should implement method: by_date_id")
    
<<<<<<< HEAD
    
=======
>>>>>>> 973ce23c1c917dfa6579b184c6b9f02c4acde0be
    @abstractmethod
    def list_all_spreadsheets(cls, initial_date: datetime, final_date: datetime) -> Dict[bool, List[Spreadsheet]]:
        raise NotImplemented("Should implement method: by_date_id")