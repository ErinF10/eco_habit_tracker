from pydantic import BaseModel
from datetime import date

class UserHabit(BaseModel):
    id: int
    start_date: date
    is_active: bool
    user_id: int
    habit_id: int