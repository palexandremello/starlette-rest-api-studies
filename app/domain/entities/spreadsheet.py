from datetime import datetime
from typing import NamedTuple


class Spreadsheet(NamedTuple):
    id: str
    filename: str
    initial_date: datetime
    final_date: datetime
    link: str
