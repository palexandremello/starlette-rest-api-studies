from starlette.applications import Starlette
from app.main.middlewares import middlewares
from app.main.routes import routes

def startup():
    print("Go on!!")

app = Starlette(debug=True, routes=routes, on_startup=[startup], middleware=middlewares)