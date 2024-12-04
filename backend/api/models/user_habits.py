from sqlalchemy import Boolean, Column, Integer, ForeignKey, Date, String
from database.base import Base

class UserHabit(Base):
    __tablename__ = 'user_habits'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    is_active = Column(Boolean)
    user_id = Column(String(100), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    habit_id = Column(Integer, ForeignKey('habits.id', ondelete='CASCADE'), nullable=False)
