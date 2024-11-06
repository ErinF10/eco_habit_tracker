from pydantic import BaseModel
from datetime import date

class UserHabit(BaseModel):
    user_id: int
    habit_id: int
    start_date: date
    is_active: bool


class CreateUserHabit(BaseModel):
    user_id: int
    habit_id: int