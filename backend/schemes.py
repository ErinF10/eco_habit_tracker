from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class User(BaseModel):
    id: int
    username: str
    email: Optional[str]
    password_hash: int
    date_created: date
    last_login: datetime

class Habit(BaseModel):
    id: int
    description: str

class UserHabit(BaseModel):
    id: int
    start_date: date
    is_active: bool
    user_id: int
    habit_id: int

"""
class HabitBase(BaseModel):
    description: str

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int

    class Config:
        orm_mode = True

class UserHabitBase(BaseModel):
    start_date: date
    is_active: bool

class UserHabitCreate(UserHabitBase):
    habit_id: int

class UserHabit(UserHabitBase):
    id: int
    user_id: int
    habit_id: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    date_created: date
    last_login: datetime
    habits: List[UserHabit] = []

    class Config:
        orm_mode = True
"""