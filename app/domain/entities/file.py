import dataclasses
from io import BytesIO

@dataclasses.dataclass
class File:
    filename: str
    size: int
    type: str
    extension: str
    content: BytesIO

    @classmethod
    def from_dict(cls, dictonary):
        return cls(**dictonary)
    
    def to_dict(self):
        return dataclasses.asdict(self)
