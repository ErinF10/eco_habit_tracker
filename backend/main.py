from fastapi import FastAPI
from api.routes import user
from api.routes import habit


app = FastAPI()

app.include_router(user.router)
app.include_router(habit.router)


# test_habits = [
#     Habit(
#         id=1,
#         description='Take the Subway'
#     )
# ]

# test_user_habits = [
#     UserHabit(
#         id = 1,
#         start_date = date.today(),
#         is_active = True,
#         user_id = 1,
#         habit_id = 1
#     )
# ]

# @app.get("/users")
# async def fetch_users():
#     """
#     Args:
#         None

#     Raises:

#     Returns:
#         The list of all users in the test_users list
#     """
#     return test_users

# @app.get("/habits/{user_id}")
# async def fetch_user_habits(user_id: int):
#     """
#     Args:
#         user_id: passed in through the get URL

#     Raises:
#         404 User not found: if the user_id in the get URL does not exist
#         404 No habits found for this user: if there are no habits that match the given user_id
        
#     Returns:
#         A list of all the habits for a specific user_id
#     """
#     # First, check if the user exists
#     user = next((user for user in test_users if user.id == user_id), None)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Find all UserHabit entries for this user
#     user_habits = [user_habit for user_habit in test_user_habits if user_habit.user_id == user_id]
    
#     if not user_habits:
#         raise HTTPException(status_code=404, detail="No habits found for this user")

#     # Get the actual Habit objects
#     habits = [(habit for habit in test_habits if habit.id == user_habit.habit_id) for user_habit in user_habits]

#     return habits