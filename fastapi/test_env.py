from starlette.config import Config

config = Config('.env')
SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')
print(type(SQLALCHEMY_DATABASE_URL))
