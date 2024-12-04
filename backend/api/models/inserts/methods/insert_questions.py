from api.models.questions import Question

def insert_survey_questions(session):
    questions = [
        # Question 1
        "What best describes your commute to work?",
        # Question 2
        "How often do you typically purchase new clothing?",
        # Question 3
        "Are you often home for the majority of the weekend?",
        # Question 4
        "In a typical week, how often do you use plastic utensils at least once throughout the day?",
        # Question 5
        "In a typical week, how often do you use and discard single-use food containers?",
        # Question 6
        "Do you bring reusable bags with you when shopping?",
        # Question 7
        "How often do you tend to purchase coffee to-go?"
    ]

    # Create a list of dictionaries for executemany
    question_data = [{"question_text": q} for q in questions]

    # Using executemany with ORM
    session.execute(
        Question.__table__.insert(),
        question_data
    )
    session.commit()

    print(f"{len(questions)} questions inserted successfully.")

