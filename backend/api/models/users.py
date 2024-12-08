from sqlalchemy import Column, Integer, String, DateTime, Date
from database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    clerk_id = Column(String(100))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    # password_hash = Column(String(20), nullable=False)
    date_created = Column(Date)
    last_login = Column(DateTime)

