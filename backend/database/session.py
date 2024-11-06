from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
import os
from dotenv import load_dotenv
from .base import Base

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

URL_DATABASE = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Create tables
Base.metadata.create_all(bind=engine)