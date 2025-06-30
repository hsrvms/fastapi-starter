import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()

"""You can add a DATABASE_URL environment variable to your .env file"""
DATABASE_URL = os.getenv("DATABASE_URL")

"""Or hardcode SQLite here"""
# DATABASE_URL = "sqlite:///./todosapp.db"

"""Or hardcode PostgreSQL here"""
# DATABASE_URL = "postgresql://postgres:postgres@db:5432/cleanfastapi"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]
