from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os

# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:feFsfZ3bV51O7F9F1ASZ@containers-us-west-89.railway.app:5665/railway"
SQLALCHEMY_DATABASE_URI = "mysql://root:jMAoJVX7Ie6NOYF1GEct@containers-us-west-102.railway.app:6998/railway"

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
