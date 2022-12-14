
from typing import Dict, List, Type
from app.domain.entities.spreadsheet import Spreadsheet
from app.domain.usecases.create_spreadsheet import CreateSpreadsheet as CreateSpreadsheetInterface
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface as SpreadsheetRepository


class CreateSpreadsheet(CreateSpreadsheetInterface):
    def __init__(self, spreadsheet_repository: Type[SpreadsheetRepository]):
        self.spreadsheet_repository = spreadsheet_repository
    
    def create(self, filename: str, initial_date: str, final_date: str, status: int) -> Dict[bool, List[Spreadsheet]]:
        response = None
        validate_entry = isinstance(filename, str) and isinstance(initial_date, str) and isinstance(final_date, str)
        if validate_entry:
            response = self.spreadsheet_repository.insert_spreadsheet(filename, initial_date, final_date, status)
        
        return {"success": validate_entry, "data": response}
