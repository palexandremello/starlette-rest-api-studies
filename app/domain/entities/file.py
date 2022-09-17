import dataclasses

@dataclasses.dataclass
class File:
    filename: str
    size: int
    type: str
    extension: str
    content: bytes

    @classmethod
    def from_dict(cls, dictonary):
        return cls(**dictonary)
    
    def to_dict(self):
        return dataclasses.asdict(self)
