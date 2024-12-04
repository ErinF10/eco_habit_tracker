from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class User(BaseModel):
    id: str
    clerk_id: str
    username: str
    email: Optional[str] = None
    # password_hash: Optional[str] = 'test'
    date_created: date
    last_login: datetime

class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None
    # password: Optional[str] = 'test'

class UsernameUpdateRequest(BaseModel):
    username: str

class UserEmailUpdateRequest(BaseModel):
    email: str
