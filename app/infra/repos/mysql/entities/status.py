from sqlalchemy import Column, Integer, DateTime, text, String
from app.infra.repos.config import Base 

class Status(Base):

    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=False)
    created_at = Column(DateTime, server_default=text('now()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('now()'), nullable=False)


    def __repr__(self) -> str:
        return f"Status[name=({self.name})]"