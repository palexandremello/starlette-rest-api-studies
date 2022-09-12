from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middlewares = [
    Middleware(CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['POST', 'GET'],
    allow_headers=['access-control-allow-origin', 'authorization', 'content-type'],

),
]
