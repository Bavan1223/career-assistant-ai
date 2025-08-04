def run_conversation():
    intro_questions = get_intro_questions()
    user_data = {}

    # Intro round
    for q in intro_questions:
        print("AI:", q)
        user_input = input("You: ")
        user_data[q] = user_input

    # Follow-up round
    followup_questions = get_followup_questions(user_data)
    for q in followup_questions:
        print("AI:", q)
        user_input = input("You: ")
        user_data[q] = user_input

    # Save all
    save_user_data(user_data)

if __name__ == "__main__":
    run_conversation()
