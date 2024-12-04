from sqlalchemy import Column, Integer, String, ForeignKey
from database.base import Base

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id', ondelete='CASCADE'))
    answer_text = Column(String(255))