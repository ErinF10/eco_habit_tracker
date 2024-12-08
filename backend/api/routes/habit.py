from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.schemas.habit_schema import Habit
from api.models.habits import Habit as HabitModel
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
        

        

