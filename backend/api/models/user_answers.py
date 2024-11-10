from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database.base import Base

class UserAnswer(Base):
    __tablename__ = 'user_answers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    answered_at = Column(DateTime)