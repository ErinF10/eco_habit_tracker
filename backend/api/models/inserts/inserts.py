from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.session import get_db
from .methods.insert_questions import insert_survey_questions
from .methods.insert_answers import insert_answers
from .methods.insert_habits import insert_habits
from .methods.insert_habit_suggestions import insert_habit_suggestions
from api.models.habits import Habit

router = APIRouter(tags=['inserts'])

@router.post("/inserts/insert_questions")
def api_insert_questions(session: Session = Depends(get_db)):
    insert_survey_questions(session)
    return {"message": "Survey questions inserted successfully"}

@router.post("/insert_answers")
def api_insert_answers(session: Session = Depends(get_db)):
    insert_answers(session)
    return {"message": "Survey answers inserted successfully"}

@router.post('/insert/insert_habits')
def api_insert_habtis(session: Session = Depends(get_db)):
    insert_habits(session)
    return {"message": "Habits inserted successfully"}

@router.post('/insert/insert_habit_suggestions')
def api_insert_habit_suggestions(session: Session = Depends(get_db)):
    insert_habit_suggestions(session)
    return {"message": "Habit suggestions inserted successfully"}

@router.delete("/delete_habits")
def delete_all_rows(db: Session = Depends(get_db)):
    db.query(Habit).delete()
    db.commit()
    return {"message": "All rows deleted successfully"}