from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Date
from database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    password_hash = Column(Integer, nullable=False)
    date_created = Column(Date)
    last_login = Column(DateTime)

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)


class UserHabit(Base):
    __tablename__ = 'user_habits'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    is_active = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    habit_id = Column(Integer, ForeignKey('habits.id'), nullable=False)


