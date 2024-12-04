from fastapi import FastAPI
from api.routes import user
from api.routes import habit
from api.routes import user_habit
from api.models.inserts import inserts


app = FastAPI()

app.include_router(user.router)
app.include_router(habit.router)
app.include_router(user_habit.router)
app.include_router(inserts.router)

