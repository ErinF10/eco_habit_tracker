from fastapi import HTTPException, status, APIRouter
from database.session import db_dependency
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from api.schemas.user_schema import UserCreate, UsernameUpdateRequest, UserEmailUpdateRequest
from api.models.users import User as UserModel
from datetime import date, datetime


router = APIRouter(tags=['users'])

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: db_dependency):
    """
        Args:
            user_id: User ID wanted to be returned
        Raises:
            404: User not found
        Returns:
            user: Details for the specified user

    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: db_dependency):
    """
    Args:
        user: Username, email, and password for the new user.
    Raises:
        400: Error Creating User
    Returns:
        dict: id, username, and email of new user.
    """
    new_user = UserModel(
        username=user.username,
        email=user.email,
        password_hash=user.password,
        date_created=date.today(),
        last_login=datetime.now()
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating user")
    
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    """
        Args:
            user_id: User ID for user wanted to be deleted
        Raises: 
            404: User not found
            500: Internal server error
        Returns: 
            dict: Positive message if successful
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        db.delete(user)
        db.commit()
    except SQLAlchemyError:
        db.rollback
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occured while deleting the user")
    
    return {"message": "User successfully deleted"}


@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_username(user_id: int, username_update: UsernameUpdateRequest, db: db_dependency):
    """
        Args:
            user_id (int): ID of the user to be updated
            username_update (UsernameUpdateRequest): Updated username
        Raises:
            404: User not found
            400: Username already exists
            500: Any internal database errors
        Returns:
            dict: A message confirming the update and the new username
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if user.username == username_update.username:
        return {"message": "Username is unchanged", "username": user.username}

    try:
        user.username = username_update.username
        db.commit()
        return {"message": "Username updated successfully", "username": user.username}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.put("/users/{user_id}/email")
async def update_email(user_id: int, email_update: UserEmailUpdateRequest, db: db_dependency):
    """
        Args:
            user_id (int): ID of the user to be updated
            email_update (UserEmailUpdateRequest): Updated email
        Raises:
            404: User not found
            400: Email already exists
            500: Any internal database errors
        Returns:
            dict: A message confirming the update and the new email
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if user.email == email_update.email:
        return {"message": "Email is unchanged", "email": user.email}

    try:
        user.email = email_update.email
        db.commit()
        return {"message": "Email updated successfully", "email": user.email}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
