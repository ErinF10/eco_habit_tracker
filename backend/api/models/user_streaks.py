from sqlalchemy import Column, Integer, ForeignKey
from database.base import Base


class UserStreak(Base):
    __tablename__ = 'user_streaks'

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    current_streak = Column(Integer)
    best_streak = Column(Integer)