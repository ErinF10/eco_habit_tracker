from sqlalchemy import Column, Integer, Boolean, ForeignKey
from database.base import Base

class UserHabitSchedule(Base):
    __tablename__ = 'user_habit_schedules'

    id = Column(Integer, primary_key=True)
    user_habit_id = Column(Integer, ForeignKey('user_habits.id'))
    monday = Column(Boolean)
    tuesday = Column(Boolean)
    wednesday = Column(Boolean)
    thursday = Column(Boolean)
    friday = Column(Boolean)
    saturday = Column(Boolean)
    sunday = Column(Boolean)