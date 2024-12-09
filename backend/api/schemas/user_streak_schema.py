from pydantic import BaseModel

class CreateUserStreak(BaseModel):
    user_id: int