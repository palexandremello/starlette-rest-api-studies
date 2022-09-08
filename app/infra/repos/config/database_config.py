import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = os.environ['DATABASE_STRING_URL']
        self.session = None
    

    def get_engine(self):
        return create_engine(self.__connection_string)
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()