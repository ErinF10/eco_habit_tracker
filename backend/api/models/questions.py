from sqlalchemy import Column, Integer, String
from database.base import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String(255))