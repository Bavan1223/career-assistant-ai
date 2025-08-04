def get_followup_questions(user_data):
    followup_questions = []

    # Check based on previous answers
    name = user_data.get("What is your name?")
    goal = user_data.get("What is your goal?")
    experience = user_data.get("Do you have experience in coding or tech field?")

    if goal and "job" in goal.lower():
        if experience and experience.lower() in ["no", "not much", "beginner"]:
            followup_questions.append("What are you interested in? (e.g., Web Dev, Data Science, etc.)")
            followup_questions.append("Do you want a study roadmap or project guidance?")
        else:
            followup_questions.append("Do you have a resume ready?")
            followup_questions.append("Which companies are you aiming for?")
    elif goal and "learning" in goal.lower():
        followup_questions.append("Which year of engineering are you in?")
        followup_questions.append("Are you comfortable with coding or just starting?")
    else:
        followup_questions.append("What kind of help do you expect from me?")

    return followup_questions
