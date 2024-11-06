from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.schemas.habit_schema import Habit
from api.models.user_habits import UserHabit as UserHabitModel
from api.models.users import User as UserModel
from api.services.get_user_habits import get_user_habits_for_user
from datetime import date

router = APIRouter(tags=['userhabits'])

@router.post("/userhabits/{user_id}/{habit_id}", status_code=status.HTTP_201_CREATED)
async def create_user_habit(user_id: int, habit_id: int, db: db_dependency):
    """
        Args:
            user_id (int): ID for the user the habit will correspond to.
            habit_id (int): ID for the corresponding habit
        Raises:
            400: Error creating user habit
        Returns:
            dict: The new user habit
    """
    new_user_habit = UserHabitModel(
        habit_id = habit_id,
        user_id = user_id,
        start_date = date.today(),
        is_active = True
    )
    try:
        db.add(new_user_habit)
        db.commit()
        db.refresh(new_user_habit)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user habit")
    return {"new_user_habit": new_user_habit}


@router.get("/userhabits/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_habits(user_id: int, db: db_dependency):
    """
        Args:
            user_id: passed in through the get URL

        Raises:
            404 User not found: if the user_id in the get URL does not exist
                        
        Returns:
            A list of all the habits for a specific user_id
    """
    return get_user_habits_for_user(user_id, db)


