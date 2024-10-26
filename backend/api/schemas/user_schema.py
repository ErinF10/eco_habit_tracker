from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class User(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    password_hash: int
    date_created: date
    last_login: datetime