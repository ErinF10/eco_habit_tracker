from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from database.base import Base

class UserAnswer(Base):
    __tablename__ = 'user_answers'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), ForeignKey('users.id', ondelete='CASCADE'))
    answer_id = Column(Integer, ForeignKey('answers.id', ondelete='CASCADE'))
    answered_at = Column(DateTime)