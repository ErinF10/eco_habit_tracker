from api.models.habits import Habit

def insert_habits(session):
    habits = [
        "Consider walking, biking, or using public transportation for your commute.",
        "Organize a carpool with colleagues who live nearby.",
        "Unplug and power off work devices at the end of the day.",
        "Maximize natural lighting and reduce artificial light usage for at least one hour daily.",
        "Plan an at home or local activity that reduces travel time.",
        "Explore second-hand stores or thrift shops for clothing instead of purchasing new items weekly.",
        "Adopt a \"quality over quantity\" approach to shopping; limit clothing purchases to 1 or less items this week.",
        "Donate one clothing item for each new clothing item purchased.",
        "Carry reusable utensils with you for meals on-the-go.",
        "Encourage a friend or family member to bring reusable utensils.",
        "Use reusable food containers for packed lunches or leftovers.",
        "Learn to make one of your favorite takeout meals at home each week.",
        "Meal prep once a week to reduce waste.",
        "Encourage a friend or family member to use reusable food containers.",
        "Bring reusable bags with you to the store.",
        "Set a reminder to bring reusable bags before your grocery trips.",
        "Carry reusable straws with you and use them in place of plastic straws.",
        "Invest in a reusable coffee cup for your to-go beverages and bring the cup with you.",
        "Learn to make your favorite coffee drink at home."
    ]

    habit_data = [{"description": habit} for habit in habits]

    session.execute(
        Habit.__table__.insert(),
        habit_data
    )
    session.commit()







