from sqlalchemy import Column, Integer, String
from database.base import Base

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)
