import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", default="").split(",")


class DBConfig:
    HOST = os.getenv("DB_HOST", default="127.0.0.1:5432")
    NAME = os.getenv("DB_NAME", 'silsilah')
    USERNAME = os.getenv("DB_USERNAME", 'silsilah')
    PASSWORD = os.getenv("DB_PASSWORD", 'mysecretpassword')