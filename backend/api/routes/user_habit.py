from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.schemas.habit_schema import Habit
from api.models.user_habits import UserHabit as UserHabitModel
from api.schemas.user_habit_schema import CreateUserHabit as CreateUserHabit
from api.models.users import User as UserModel
from api.services.get_user_habits import get_user_habits_for_user
from datetime import date
from sqlalchemy import and_

router = APIRouter(tags=['userhabits'])

@router.post("/userhabits", status_code=status.HTTP_201_CREATED)
async def create_user_habit(newHabit: CreateUserHabit, db: db_dependency):
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
        habit_id = newHabit.habit_id,
        user_id = newHabit.user_id,
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


@router.get("/userhabits/user/{user_id}", status_code=status.HTTP_200_OK)
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

# @router.get("/userhabits/{user_id}/{habit_id}")
# async def 

@router.delete("/userhabits/{user_id}/{habit_id}", status_code=status.HTTP_200_OK)
async def delete_user_habit(user_id: int, habit_id: int, db: db_dependency):
    """
        Args:
            user_id: User ID for user habit wanted to be deleted
            habit_id: Habit ID for user habit wanted to be deleted
        Raises: 
            404: User habit not found
            500: Internal server error
        Returns: 
            dict: Positive message if successful
    """
    user_habit = db.query(UserHabitModel).filter(
        and_(
            UserHabitModel.user_id == user_id,
            UserHabitModel.habit_id == habit_id
        )
    ).first()    
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    try:
        db.delete(user_habit)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occured while deleting the user habit")
    
@router.get("/userhabits/{user_id}/{habit_id}", status_code=status.HTTP_200_OK)
async def get_user_habits(user_id: int, habit_id: int, db: db_dependency):
    """
        Args:
            user_id: passed in through the get URL, id of the user
            habit_id: id of the habit
        Raises:
            404 User not found: if the user_id or habit_id in the get URL does not exist
                        
        Returns:
            The user habit matching the user id and habit id
    """
    user_habit = db.query(UserHabitModel).filter(
        and_(
            UserHabitModel.user_id == user_id,
            UserHabitModel.habit_id == habit_id
        )
    ).first()    
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    return user_habit

@router.get("/userhabits/{user_habit_id}", status_code=status.HTTP_200_OK)
async def get_user_habit_by_id(user_habit_id: int, db: db_dependency):
    """
        Args:
            user_habit_id: id of the user habit
        Raises:
            404 User not found: if the user_habit_id in the get URL does not exist
                        
        Returns:
            The user habit matching the user habit id
    """
    user_habit = db.query(UserHabitModel).filter(UserHabitModel.id == user_habit_id).first()    
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    return user_habit