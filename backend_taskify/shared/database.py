from dotenv import load_dotenv
import os
# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

load_dotenv()

TOKEN = os.getenv("TOKEN")

engine = create_async_engine(
    TOKEN
)
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
