from pydantic import BaseModel

class UserHabitSchedule(BaseModel):
    user_habit_id: int
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool

class CreateHabitSchedule(BaseModel):
    user_habit_id: int