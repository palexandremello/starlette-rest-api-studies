
from typing import List
from app.application.errors.validation import InvalidSpreadsheetError
from app.application.helpers.dataframe import Dataframe
from app.application.validation.validator import Validator


class SpreadsheetIntegration(Validator):
    def __init__(self, dataframe, allowed_columns: List[str]) -> None:
        self.dataframe = dataframe
        self.allowed_columns : Dataframe = {
            "columns": allowed_columns
        }

    def validate(self) -> Exception or None:
        return None if self.is_have_all_columns() else InvalidSpreadsheetError(self.allowed_columns['columns'])

    def is_have_all_columns(self) -> List[str]:
        difference_columns = set(self.dataframe.columns) - set(self.allowed_columns['columns'])
        return False if len(difference_columns) != 0 else True