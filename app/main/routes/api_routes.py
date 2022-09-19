from app.main.routes.create_spreadsheet_route import create_spreadsheet
from app.main.routes.list_spreadsheet_route import list_spreadsheet
from starlette.routing import Route, Mount

routes = [
    Mount('/v1/api/spreadsheet',routes=[
        Route('/send', create_spreadsheet, methods=['POST']),
        Route('/list', list_spreadsheet, methods=['GET']),
    ])
]