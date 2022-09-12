from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, text, String
from sqlalchemy.orm import relationship
from app.infra.repos.config import Base
from app.infra.repos.mysql.entities.status import Status 

class Spreadsheet(Base):

    __tablename__ = "spreadsheet"

    id = Column(Integer, primary_key=True)
    initial_date = Column(DateTime, nullable=False, unique=False)
    final_date = Column(DateTime, nullable=False, unique=False)
    filename = Column(String, nullable=False, unique=False)
    link = Column(Text, nullable=True, unique=False)
    path = Column(Text, nullable=False, unique=False)
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship(Status)
    created_at = Column(DateTime, server_default=text('now()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('now()'), nullable=False)




    def __repr__(self) -> str:
        return f"Spreadsheet [filename=({self.filename})]"
