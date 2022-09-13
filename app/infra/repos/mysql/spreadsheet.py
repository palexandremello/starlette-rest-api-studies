from datetime import datetime
from typing import List
from app.data.interfaces.spreadsheet_repository_interface import SpreadsheetRepositoryInterface
from app.infra.repos.config.database_config import DatabaseConnectionHandler
from app.infra.repos.mysql.entities.spreasheet import Spreadsheet
from app.domain.entities.spreadsheet import Spreadsheet as SpreadsheetModel
from app.application.helpers.results_functions import create_array_response

class MysqlSpreadsheetRepository(SpreadsheetRepositoryInterface):
    
    @classmethod
    def insert_spreadsheet(cls, filename: str, initial_date: datetime, final_date: datetime, status_id: int) -> SpreadsheetModel:
        
        with DatabaseConnectionHandler() as database_connection:
            try:
                new_spreadsheet = Spreadsheet(filename=filename, initial_date=initial_date, final_date=final_date, status_id=status_id)
                database_connection.session.add(new_spreadsheet)
                database_connection.session.commit()

                return SpreadsheetModel(id=new_spreadsheet.id, filename=new_spreadsheet.filename,
                                        initial_date=new_spreadsheet.initial_date, final_date=new_spreadsheet.final_date,
                                        status=status_id,
                                        link=new_spreadsheet.link)
            except Exception as error:
                database_connection.session.rollback()
                raise error
            finally:
                database_connection.session.close()
            
    @classmethod
    def select_spreadsheet():
        pass

    @classmethod
    def list_spreadsheet(cls, initial_date: datetime, final_date: datetime) -> List[SpreadsheetModel]:
        with DatabaseConnectionHandler() as database_connection:
            try:
                resp = database_connection.session.query(Spreadsheet).filter(Spreadsheet.initial_date >= initial_date, Spreadsheet.final_date <= final_date).all()
                return [create_array_response(item) for item in resp] 
            except Exception as error:
                database_connection.session.rollback()
                raise error
            finally:
                database_connection.session.close()
