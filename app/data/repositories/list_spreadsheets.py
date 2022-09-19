
from typing import Dict, List, Type
from app.domain.entities.spreadsheet import Spreadsheet
from app.domain.usecases.list_spreadsheet import ListSpreadsheet as ListSpreadsheetInterface
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface as SpreadsheetRepository


class ListSpreadsheet(ListSpreadsheetInterface):
    def __init__(self, spreadsheet_repository: Type[SpreadsheetRepository]):
        self.spreadsheet_repository = spreadsheet_repository
    
    def list_spreadsheets_by_date(self, initial_date: str, final_date: str) -> Dict[bool, List[Spreadsheet]]:
        response = None
        validate_entry = initial_date <= final_date
       
        if validate_entry:
            response = self.spreadsheet_repository.list_spreadsheet(initial_date, final_date)
        
        return {"success": validate_entry, "data": response}

    def list_all_spreadsheets(self):
        try:
            response = self.spreadsheet_repository.list_spreadsheet()
            return {"success": True, "data": response}
        except Exception:
<<<<<<< HEAD
            return {"success": false, "data": None}
=======
            return {"success": False, "data": None}
>>>>>>> 973ce23c1c917dfa6579b184c6b9f02c4acde0be
