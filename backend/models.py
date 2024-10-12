from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String)
    password_hash = Column(Integer, nullable=False)
    date_created = Column(DateTime)
    last_login = Column(DateTime)

class UserHabit(Base):
    __tablename__ = 'user_habits'

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    is_active = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    habit_id = Column(Integer, ForeignKey('habits.id'), nullable=False)

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

