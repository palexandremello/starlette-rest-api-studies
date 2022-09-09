from app.main.interface.route import RouteInterface
from app.infra.repos.mysql.spreadsheet import MysqlSpreadsheetRepository as SpreadsheeRepository
from app.data.repositories.create_spreadsheet import CreateSpreadsheet
from app.application.controllers.create_spreadsheet_controller import CreateSpreadsheetController

def create_spreadsheet_composer():
    """ Composing Insert Spreadsheet Route
    :param - None
    :return - Object with Insert Spreadsheet Route
    """

    print("aqui")
    repository = SpreadsheeRepository()
    use_case = CreateSpreadsheet(repository)
    create_spreadsheet_route = CreateSpreadsheetController(use_case)

    return create_spreadsheet_route