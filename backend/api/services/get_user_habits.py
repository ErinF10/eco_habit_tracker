from fastapi import HTTPException, status
from api.models.user_habits import UserHabit as UserHabitModel
from api.models.users import User as UserModel
from api.models.habits import Habit as HabitModel
from sqlalchemy.orm import joinedload


def get_user_habits_for_user(user_id, db):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # user_habits = db.query(UserHabitModel).filter(UserHabitModel.user_id == user_id)
    # if not user_habits:
    #     raise HTTPException(status_code=404, detail="No habits found for this user")
    
    # habits = db.query(HabitModel).filter(HabitModel.id == user_habits.habit_id)

    # # Query user habits with joined habit details
    # user_habits = db.query(UserHabitModel)\
    #     .join(HabitModel)\
    #     .options(joinedload(UserHabitModel.habit_id))\
    #     .filter(UserHabitModel.user_id == user_id)\
    #     .all()
    
    # # If you want to return just the habits, not the UserHabit objects:
    # habits = [user_habit.habit for user_habit in user_habits]
    
    return habits

    