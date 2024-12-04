from api.models.habit_suggestions import HabitSuggestion

def insert_habit_suggestions(session):
    habit_suggestions = [
        # Commute-related suggestions
        {"habit_id": 22, "answer_id": 1},  # Consider walking, biking, or using public transportation for your commute.
        {"habit_id": 23, "answer_id": 1},  # Organize a carpool with colleagues who live nearby.
        {"habit_id": 24, "answer_id": 3},  # Unplug and power off work devices at the end of the day.
        {"habit_id": 25, "answer_id": 3},  # Maximize natural lighting and reduce artificial light usage for at least one hour daily.

        # Clothing purchase suggestions
        {"habit_id": 27, "answer_id": 5},  # Explore second-hand stores or thrift shops for clothing instead of purchasing new items weekly.
        {"habit_id": 28, "answer_id": 5},  # Adopt a "quality over quantity" approach to shopping; limit clothing purchases to 1 or less items this week.
        {"habit_id": 29, "answer_id": 6},  # Donate one clothing item for each new clothing item purchased.
        
        # Weekend questions
        {"habit_id": 25, "answer_id": 8},  # Maximize natural lighting and reduce artificial light usage for at least one hour daily.
        {"habit_id": 26, "answer_id": 9},  # Plan an at home or local activity that reduces travel time.

        # Plastic utensil usage suggestions
        {"habit_id": 30, "answer_id": 11},  # Carry reusable utensils with you for meals on-the-go.
        {"habit_id": 30, "answer_id": 12},  # Carry reusable utensils with you for meals on-the-go.
        {"habit_id": 31, "answer_id": 10},  # Encourage a friend or family member to bring reusable utensils.

        # Food container usage suggestions
        {"habit_id": 32, "answer_id": 14},  # Use reusable food containers for packed lunches or leftovers.
        {"habit_id": 33, "answer_id": 14},  # Learn to make one of your favorite takeout meals at home each week.
        {"habit_id": 34, "answer_id": 14},  # Meal prep once a week to reduce waste.
        {"habit_id": 34, "answer_id": 15},  # Meal prep once a week to reduce waste.
        {"habit_id": 32, "answer_id": 15},  # Use reusable food containers for packed lunches or leftovers.
        {"habit_id": 33, "answer_id": 15},  # Learn to make one of your favorite takeout meals at home each week.
        {"habit_id": 35, "answer_id": 13},  # Encourage a friend or family member to use reusable food containers.

        # Reusable bag usage suggestions
        {"habit_id": 36, "answer_id": 17},  # Bring reusable bags with you to the store.
        {"habit_id": 37, "answer_id": 18},  # Set a reminder to bring reusable bags before your grocery trips.

        # Coffee to-go suggestions
        {"habit_id": 38, "answer_id": 20},  # Carry reusable straws with you and use them in place of plastic straws.
        {"habit_id": 39, "answer_id": 20},  # Invest in a reusable coffee cup for your to-go beverages and bring the cup with you.
        {"habit_id": 40, "answer_id": 20},  # Learn to make your favorite coffee drink at home.
        {"habit_id": 38, "answer_id": 21},  # Carry reusable straws with you and use them in place of plastic straws.
        {"habit_id": 39, "answer_id": 21},  # Invest in a reusable coffee cup for your to-go beverages and bring the cup with you.
        {"habit_id": 40, "answer_id": 21},  # Learn to make your favorite coffee drink at home.
    ]

    session.execute(
        HabitSuggestion.__table__.insert(),
        habit_suggestions
    )
    session.commit()

    print(f"{len(habit_suggestions)} habit suggestions inserted successfully.")