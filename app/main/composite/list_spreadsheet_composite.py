from app.main.interface.route import RouteInterface
from app.infra.repos.mysql.spreadsheet import MysqlSpreadsheetRepository as SpreadsheeRepository
from app.data.repositories.list_spreadsheets import ListSpreadsheet
from app.application.controllers.list_spreadsheet_controller import ListSpreadsheetController 

def list_spreadsheet_composer():
    """ Composing Insert Spreadsheet Route
    :param - None
    :return - Object with Insert Spreadsheet Route
    """

    repository = SpreadsheeRepository()
    use_case = ListSpreadsheet(repository)
    list_spreadsheet_route = ListSpreadsheetController(use_case)
    return list_spreadsheet_route