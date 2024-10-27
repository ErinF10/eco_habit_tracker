from fastapi import HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.session import db_dependency

from api.schemas.habit_schema import Habit
from api.services.get_user_habits import get_user_habits_for_user

router = APIRouter(tags=['habits'])

@router.post("/habits/{user_id}/{habit_id}", status_code=status.HTTP_201_CREATED)
async def create_habit(user_id: int, habit_id: int, )

# @router.get("/habits/{user_id}")
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
#     return get_user_habits_for_user(user_id, test_habits, test_users, test_user_habits)
@router.get("/habits/{user_id}", status_code=status.HTTP_200_OK)

