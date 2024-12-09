from fastapi import HTTPException, status
from api.models.user_habits import UserHabit as UserHabitModel
from api.models.users import User as UserModel
from api.models.habits import Habit as HabitModel

def get_user_habits_for_user(user_id, db):
    # user = db.query(UserModel).filter(UserModel.id == user_id).first()
    # if user is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user_habits = db.query(UserHabitModel).filter(UserHabitModel.user_id == user_id).all()
    
    return user_habits

    