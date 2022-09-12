from sqlalchemy import Column, String, Integer, Text, DateTime
from app.infra.repos.config import Base 

class Spreadsheet(Base):

    __tablename__ = "spreadsheet"

    id = Column(Integer, primary_key=True)
    filename = Column(Text, nullable=False, unique=False)
    initial_date = Column(DateTime, nullable=False, unique=False)
    final_date = Column(DateTime, nullable=False, unique=False)
    link = Column(Text, nullable=True, unique=False)


    def __repr__(self) -> str:
        return f"Spreadsheet [filename=({self.filename})]"
