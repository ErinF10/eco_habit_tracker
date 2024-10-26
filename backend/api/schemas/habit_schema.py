from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class Habit(BaseModel):
    id: int
    description: str