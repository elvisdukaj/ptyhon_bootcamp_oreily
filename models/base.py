import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from app.config import Settings

Base = declarative_base()
settings = Settings()

engine = create_engine(settings.db_host, echo=True)


def recreate_postgres_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
