from sqlalchemy import create_engine
from models.base_model import Base
from os import getenv

database_url = getenv('DATABASE_URL')
engine = create_engine(database_url)
