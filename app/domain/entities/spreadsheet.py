import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Spreadsheet:
    id: int
    filename: str
    initial_date: datetime
    final_date: datetime
    link: str


    @classmethod
    def from_dict(cls, dictonary):
        return cls(**dictonary)
    
    def to_dict(self):
        return dataclasses.asdict(self)