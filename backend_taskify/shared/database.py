from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

TOKEN_SQLALCHEMY = os.getenv("TOKEN_SQLALCHEMY")

engine = create_engine(
    TOKEN_SQLALCHEMY
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
