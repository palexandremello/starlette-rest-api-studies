import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Spreadsheet:
    id: int
    filename: str
    initial_date: datetime
    final_date: datetime
    status: int
    link: str
    path: str 
    status_id: int
    status: str
    created_at: datetime
    updated_at: datetime


    @classmethod
    def from_dict(cls, dictonary):
        return cls(**dictonary)
    
    def to_dict(self):
        return dataclasses.asdict(self)
        