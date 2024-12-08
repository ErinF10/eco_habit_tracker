from fastapi import FastAPI
from api.routes import user
from api.routes import habit
from api.routes import user_habit
from api.routes import user_streak
from api.models.inserts import inserts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5175",
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(habit.router)
app.include_router(user_habit.router)
app.include_router(user_streak.router)
app.include_router(inserts.router)


