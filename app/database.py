import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DBConfig


host = DBConfig.HOST
name = DBConfig.NAME
username = urllib.parse.quote(DBConfig.USERNAME, safe="")
password = urllib.parse.quote(DBConfig.PASSWORD, safe="")

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()