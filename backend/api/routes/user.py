from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from fastapi import FastAPI , HTTPException, Depends, status, APIRouter
from api.services import get_users
from api.schemas.user_schema import User
from api.schemas.user_habit_schema import UserHabit

# app = FastAPI()
router = APIRouter(tags=['users'])

test_users = [
    User(
        id=1,
        username='erinforrest',
        password_hash=1234,
        date_created=date.today(),
        last_login=datetime.now()
    )
]

test_user_habits = [
    UserHabit(
        id = 1,
        start_date = date.today(),
        is_active = True,
        user_id = 1,
        habit_id = 1
    )
]

@router.get("/users")
async def fetch_users():
    """
    Args:
        None

    Raises:

    Returns:
        The list of all users in the test_users list
    """
    return get_users.get_all_users(test_users)