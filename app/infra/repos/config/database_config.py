import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnectionHandler:
    def __init__(self) -> None:
        database_driver = os.environ['DATABASE_DRIVER']
        database_user = os.environ['DATABASE_USER']
        database_password = os.environ['DATABASE_PASSWORD']
        database_url = os.environ['DATABASE_URL']
        database_name = os.environ['DATABASE_NAME']
        self.__connection_string = f"{database_driver}://{database_user}:{database_password}@{database_url}/{database_name}"
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