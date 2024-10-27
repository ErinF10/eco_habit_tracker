from fastapi import HTTPException

def get_user_habits_for_user(user_id, test_habits, test_users, test_user_habits):
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