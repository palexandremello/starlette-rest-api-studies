import sys
import pytest
import os
from sqlalchemy_utils import drop_database
from app.infra.repos.config import DatabaseConnectionHandler, Base
sys.path[0] = "app"

@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    database_handler = DatabaseConnectionHandler()
    engine = database_handler.get_engine()
    Base.metadata.create_all(engine)
    yield                            # Run the tests.
    drop_database(os.environ['DATABASE_STRING_URL'])               # Drop the test database.
