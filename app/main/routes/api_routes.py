from app.main.routes.create_spreadsheet_route import create_spreadsheet
from starlette.routing import Route, Mount

routes = [
    Mount('/v1/api/spreadsheet',routes=[
        Route('/', create_spreadsheet, methods=['POST'])
    ])
]