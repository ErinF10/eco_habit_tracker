from fastapi import FastAPI , HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import User, Habit, UserHabit
from datetime import date, datetime

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

test_users = [
    User(
        id=1,
        username='erinforrest',
        password_hash=1234,
        date_created=date.today(),
        last_login=datetime.now()
    )
]

test_habits = [
    Habit(
        id=1,
        description='Take the Subway'
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

@app.get("/users")
async def fetch_users():
    """
    Args:
        None

    Raises:

    Returns:
        The list of all users in teh test_users list
    """
    return test_users

@app.get("/habits/{user_id}")
async def fetch_user_habits(user_id: int):
    """
    Args:
        user_id: passed in through the get URL

    Raises:
        404 User not found: if the user_id in the get URL does not exist
        404 No habits found for this user: if there are no habits that match the given user_id
        
    Returns:
        A list of all the habits for a specific user_id
    """
    # First, check if the user exists
    user = next((user for user in test_users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Find all UserHabit entries for this user
    user_habits = [user_habit for user_habit in test_user_habits if user_habit.user_id == user_id]
    
    if not user_habits:
        raise HTTPException(status_code=404, detail="No habits found for this user")

    # Get the actual Habit objects
    habits = [(habit for habit in test_habits if habit.id == user_habit.habit_id) for user_habit in user_habits]

    return habits