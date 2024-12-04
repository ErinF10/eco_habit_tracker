from api.models.answers import Answer

def insert_answers(session):
    answers = [
        {"question_id": 1, "answer_text": "I drive alone"},
        {"question_id": 1, "answer_text": "I use alternative transportation (carpool, public transit, bike, walk)"},
        {"question_id": 1, "answer_text": "I work from home"},
        {"question_id": 1, "answer_text": "Not applicable"},
        {"question_id": 2, "answer_text": "More than once a month"},
        {"question_id": 2, "answer_text": "About once a month"},
        {"question_id": 2, "answer_text": "Less than once a month"},
        {"question_id": 3, "answer_text": "Yes"},
        {"question_id": 3, "answer_text": "No"},
        {"question_id": 4, "answer_text": "Never"},
        {"question_id": 4, "answer_text": "1-3"},
        {"question_id": 4, "answer_text": "4-7"},
        {"question_id": 5, "answer_text": "Never"},
        {"question_id": 5, "answer_text": "1-3"},
        {"question_id": 5, "answer_text": "4-7"},
        {"question_id": 6, "answer_text": "Yes"},
        {"question_id": 6, "answer_text": "No"},
        {"question_id": 6, "answer_text": "Sometimes"},
        {"question_id": 7, "answer_text": "Never"},
        {"question_id": 7, "answer_text": "1-3 times a week"},
        {"question_id": 7, "answer_text": "4-7 times a week"}
    ]

    session.execute(
        Answer.__table__.insert(),
        answers
    )
    session.commit()

    print(f"{len(answers)} answers inserted successfully.")