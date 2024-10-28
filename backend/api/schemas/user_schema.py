from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class User(BaseModel):
    username: str
    email: Optional[str] = None
    password_hash: str
    date_created: date
    last_login: datetime

class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None
    password: str

class UsernameUpdateRequest(BaseModel):
    username: str

class UserEmailUpdateRequest(BaseModel):
    email: str
