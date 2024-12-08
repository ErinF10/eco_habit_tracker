from api.models.users import User as UserModel
from api.models.user_streaks import UserStreak as UserStreakModel
from fastapi import HTTPException, status

def update_streaks(user_id, curr_streak, best_streak, db):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    

    

