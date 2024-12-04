from sqlalchemy import Column, Integer, ForeignKey
from database.base import Base

class HabitSuggestion(Base):
    __tablename__ = 'habit_suggestions'

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey('habits.id', ondelete='CASCADE'))
    answer_id = Column(Integer, ForeignKey('answers.id', ondelete='CASCADE'))