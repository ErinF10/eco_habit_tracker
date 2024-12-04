from sqlalchemy import Column, Integer, Date, Enum, ForeignKey
from database.base import Base

class UserHabitProgress(Base):
    __tablename__ = 'user_habit_progress'

    id = Column(Integer, primary_key=True)
    user_habit_id = Column(Integer, ForeignKey('user_habits.id', ondelete='CASCADE'))
    week_start_date = Column(Date)
    monday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    tuesday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    wednesday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    thursday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    friday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    saturday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')
    sunday = Column(Enum('completed', 'partial', 'missed', 'not_scheduled'), default='not_scheduled')