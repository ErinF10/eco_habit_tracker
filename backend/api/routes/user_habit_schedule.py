from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.schemas.habit_schema import Habit
from api.models.user_habits import UserHabit as UserHabitModel
from api.schemas.user_habit_schema import CreateUserHabit as CreateUserHabit
from api.models.users import User as UserModel
from api.services.get_user_habits import get_user_habits_for_user
from api.models.user_habit_schedule import UserHabitSchedule as UserHabitScheduleModel
from api.schemas.user_habit_schedule_schema import CreateHabitSchedule
from datetime import date
from sqlalchemy import and_
from typing import List


router = APIRouter(tags=['userhabitschedules'])

@router.post('/userhabitschedules', status_code=status.HTTP_201_CREATED)
async def create_user_habit_schedule(user_habit_schedule: CreateHabitSchedule, db: db_dependency):
    """
    Args: 
        user_habit_id: ID fo rhte user habit relationship to have a schedule created for
    Raises:
        404: User habit not found
        400: Error creating user habit schedule
    Returns:
        dict: New user habit schedule
    """
    user_habit = db.query(UserHabitModel).filter(UserHabitModel.id == user_habit_schedule.user_habit_id).first()
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    try:
        new_user_habit_schedule = UserHabitScheduleModel(
            user_habit_id = user_habit_schedule.user_habit_id,
            monday = False,
            tuesday = False,
            wednesday = False,
            thursday = False,
            friday = False,
            saturday = False,
            sunday = False
        )
        db.add(new_user_habit_schedule)
        db.commit()
        db.refresh(new_user_habit_schedule)
        return new_user_habit_schedule
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating user habit schedule: {str(e)}")

    
@router.put('/userhabitschedules/{id}', status_code=status.HTTP_200_OK)
async def updates_user_habit_schedule(id: int, day: str, db: db_dependency):
    """
    Args:
        id: id of schedule to be updated
        day: which day of the week has been adjusted
    Raises: 

    Returns:
        dict: Updated user schedule
    """
    current_schedule = db.query(UserHabitScheduleModel).filter(UserHabitScheduleModel.id == id).first()

    if current_schedule is None:
        raise HTTPException(status_code=404, detail="No schedule found with id {id}")
    
    try:
        day_mapping = {
            'Mon': 'monday',
            'Tue': 'tuesday',
            'Wed': 'wednesday',
            'Thu': 'thursday',
            'Fri': 'friday',
            'Sat': 'saturday',
            'Sun': 'sunday'
        }
        
        if day not in day_mapping:
            raise HTTPException(status_code=400, detail="Invalid day provided")
        
        day_column = day_mapping[day]
        current_value = getattr(current_schedule, day_column)
        setattr(current_schedule, day_column, not current_value)
        
        db.commit()
        db.refresh(current_schedule)
        
        return {
            "id": current_schedule.id,
            "user_habit_id": current_schedule.user_habit_id,
            "monday": current_schedule.monday,
            "tuesday": current_schedule.tuesday,
            "wednesday": current_schedule.wednesday,
            "thursday": current_schedule.thursday,
            "friday": current_schedule.friday,
            "saturday": current_schedule.saturday,
            "sunday": current_schedule.sunday
        }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@router.get('/userhabitschedules/{user_id}/{habit_id}')
async def get_user_habit_schedule_by_ids(user_id: int, habit_id: int, db: db_dependency):
    """
    Args:
        user id: user id of schedule to be retrieved
        habit id: habit id of schedule to be retrieved
    Raises: 

    Returns:
        dict: user schedule
    """
    user_habit = db.query(UserHabitModel).filter(   
        and_(
            UserHabitModel.user_id == user_id,
            UserHabitModel.habit_id == habit_id
        )
    ).first()        
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    
    user_habit_schedule = db.query(UserHabitScheduleModel).filter(UserHabitScheduleModel.user_habit_id == user_habit.id).first()

    if user_habit_schedule is None:
        raise HTTPException(status_code=404, detail="No schedule found with id {id}")
    
    return user_habit_schedule

@router.get('/userhabitschedules/{user_habit_id}')
async def get_user_habit_schedule_by_id(user_habit_id: int, db: db_dependency):
    """
    Args:
        user id: user id of schedule to be retrieved
        habit id: habit id of schedule to be retrieved
    Raises: 

    Returns:
        dict: user schedule
    """
    user_habit = db.query(UserHabitModel).filter(UserHabitModel.id == user_habit_id).first()        
    if user_habit is None:
        raise HTTPException(status_code=404, detail="User habit not found")
    
    user_habit_schedule = db.query(UserHabitScheduleModel).filter(UserHabitScheduleModel.user_habit_id == user_habit.id).first()

    if user_habit_schedule is None:
        raise HTTPException(status_code=404, detail="No schedule found with user_habit_id {user_habit_id}")
    
    return user_habit_schedule

@router.get('/user-habit-schedules/{user_id}')
async def get_user_habit_schedules( user_id: int, db: db_dependency):
    """
    Retrieve all user habit schedules for a specific user.

    Args:
        user_id (int): The ID of the user whose schedules are to be retrieved.
    
    Returns:
        List[UserHabitSchedule]: A list of user habit schedules.
    """
    user_habits = db.query(UserHabitModel).filter(UserHabitModel.user_id == user_id).all()
    user_habit_ids = [user_habit.id for user_habit in user_habits]

    # Querying schedules that match the user habit IDs
    schedules = db.query(UserHabitScheduleModel).filter(UserHabitScheduleModel.user_habit_id.in_(user_habit_ids)).all()    
    
    if not schedules:
        raise HTTPException(status_code=404, detail="No schedules found for this user")
    
    return schedules