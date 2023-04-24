from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os

SQLALCHEMY_DATABASE_URI = "postgresql://root:unmXJYXW5Grdlw15EqqApIDPiPsdi6k1@dpg-ch3bm7esi8uk2tdil0o0-a/famwork_db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
