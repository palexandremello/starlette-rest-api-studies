from starlette.config import Config

config = Config(".env")

DATABASE_URL = config('DATABASE_STRING_URL')
LOCALSTACK_URL = config('LOCALSTACK_URL')
PORTAL_TRANSPORTADORA_BUCKET = config('PORTAL_TRANSPORTADORA_BUCKET')

