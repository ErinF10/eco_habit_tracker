from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.models.user_streaks import UserStreak as UserStreakModel
from api.services.get_user_habits import get_user_habits_for_user

router = APIRouter(tags=['userstreaks'])

@router.post('/userstreaks', status_code=status.HTTP_201_CREATED)
def initialize_new_user_streaks(user_id: int, db: db_dependency):
    """
    Args:
        user_id: id for the new user.
    Raises:
        400: Error Creating/Updating User streaks
    Returns:
        dict: id and streak values of the user.
    """
    try:
        existing_user_streak = db.query(UserStreakModel).filter(UserStreakModel.user_id == user_id).first()
        if existing_user_streak is None:
            new_user_streak = UserStreakModel(
                user_id = user_id,
                current_streak = 0,
                best_streak = 0
            )
            db.add(new_user_streak)
            db.commit()
            db.refresh(new_user_streak)
            return new_user_streak
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating user streak: {str(e)}")

@router.get('/userstreaks/{user_id}', status_code=status.HTTP_200_OK)
def get_user_streaks(user_id: int, db: db_dependency):
    """
    Args:
        user_id: id for the user.
    Raises:
        400: Error getting User streaks
    Returns:
        dict: id and streak values of the user.
    """
    user_streak = db.query(UserStreakModel).filter(UserStreakModel.user_id == user_id).first()
    if user_streak is None:
        raise HTTPException(status_code=404, detail="Streaks for this user {user_id} not found")
    return user_streak
        
        


