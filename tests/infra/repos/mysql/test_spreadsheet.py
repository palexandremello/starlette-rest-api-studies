from datetime import datetime
from unittest import mock
import pytest
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface
from app.domain.entities.status import Status
from app.infra.repos.mysql.spreadsheet import MysqlSpreadsheetRepository
from app.infra.repos.config.database_config import DatabaseConnectionHandler
from app.infra.repos.mysql.entities.spreasheet import Spreadsheet
import sqlalchemy


INITIAL_DATE = datetime(2022, 1, 1, 1)
FINAL_DATE = datetime(2022, 2, 1, 1)



def test_should_be_same_instance_SpreadsheetRepositoryInterface():
    sut = MysqlSpreadsheetRepository()

    assert isinstance(sut, SpreadsheetRepositoryInterface)


def test_should_insert_a_spreadsheet_conciliation_when_is_a_correct_data(create_test_database):
    database_connection_handler = DatabaseConnectionHandler()
    sut = MysqlSpreadsheetRepository()
    engine = database_connection_handler.get_engine()
    
    spreadsheet_conciliation = sut.insert_spreadsheet('any_filename', INITIAL_DATE, FINAL_DATE, Status.NOVO.value)
    query_spreadsheet = engine.execute(f"SELECT * FROM spreadsheet WHERE id='{spreadsheet_conciliation.id}'").fetchone()

    assert spreadsheet_conciliation.id == query_spreadsheet.id
    assert spreadsheet_conciliation.filename == query_spreadsheet.filename

def test_should_not_insert_a_spreadsheet_conciliation_when_insert_spreadsheet_throws(create_test_database):
    sut = MysqlSpreadsheetRepository()
    with mock.patch.object(sqlalchemy.orm.session.Session,'add', side_effect=Exception("ERROR")):
        with pytest.raises(Exception):
            assert sut.insert_spreadsheet('any_filename', INITIAL_DATE, FINAL_DATE, Status.NOVO.value)
