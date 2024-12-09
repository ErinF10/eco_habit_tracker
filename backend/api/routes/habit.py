from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency
from typing import List

from api.schemas.habit_schema import Habit
from api.models.habits import Habit as HabitModel
from api.schemas.user_habit_schedule_schema import UserHabitSchedule
from api.models.user_habit_schedule import UserHabitSchedule as UserHabitScheduleModel
from api.services.get_user_habits import get_user_habits_for_user

router = APIRouter(tags=['habits'])

@router.post("/habits", status_code=status.HTTP_201_CREATED)
async def create_habit(habit: Habit, db: db_dependency):
    """
        Args:
            habit (Habit): The new habit to be created
        Raises:
            400: Error creating habit
        Returns:
            dict: id and description for the new habit
    """
    new_habit = HabitModel(
        description = habit.description
    )
    try:
        db.add(new_habit)
        db.commit()
        db.refresh(new_habit)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating habit")
    return {"id": new_habit.id, "description": new_habit.description}

@router.get('/habits/{description}', status_code=status.HTTP_200_OK)
async def get_habit_by_description(description: str, db: db_dependency):
    """
        Args:
            Description: The description of the habit to be returned
        Raises:
            404: Habit with that description not found
        Returns:
            dict: id and description for the habit
    """
    habit = db.query(HabitModel).filter(HabitModel.description == description).first()
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit for the description \"{description}\" not found")
    return habit

@router.get('/habits/user/{user_id}', status_code=status.HTTP_200_OK)
async def get_habits_for_user(user_id: int, db: db_dependency):
    """
    Args:
        user_id : The id of the user whose habits are to be returned
    Raises:
        404: user with that id not found
    Returns:
        list of habits
    """
    user_habits = get_user_habits_for_user(user_id, db)
    if user_habits is None:
        raise HTTPException(status_code=404, detail="No habits found for this user.")
    user_habit_ids = [user_habit.habit_id for user_habit in user_habits]

    habits = db.query(HabitModel).filter(HabitModel.id.in_(user_habit_ids)).all()
    return habits

@router.get('/habits/user/{user_id}/{day}', status_code=status.HTTP_200_OK)
async def get_habits_for_user(user_id: int, day: str, db: db_dependency):
    """
    Args:
        user_id : The id of the user whose habits are to be returned
    Raises:
        404: user with that id not found
    Returns:
        list of habits
    """
    user_habits = get_user_habits_for_user(user_id, db)
    if user_habits is None:
        raise HTTPException(status_code=404, detail="No habits found for this user.")
    user_habit_ids = [user_habit.id for user_habit in user_habits]
    # [22,79,88,93]

    schedules = db.query(UserHabitScheduleModel).filter(UserHabitScheduleModel.user_habit_id.in_(user_habit_ids)).all() 

    todays_habits = [
        user_habit for user_habit in user_habits
        if any(
            schedule.user_habit_id == user_habit.id and getattr(schedule, day)
            for schedule in schedules
        )
    ]

    todays_habits_ids = [habit.habit_id for habit in todays_habits]
    
    habits = db.query(HabitModel).filter(HabitModel.id.in_(todays_habits_ids)).all()

    return habits



        

