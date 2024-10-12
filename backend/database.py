from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:password@localhost:3306/EcoHabitTracker'

engine = creat_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

Base = declarative_base()
