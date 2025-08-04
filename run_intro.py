from core.conversation.intro_conversation import get_intro_questions
from core.save_user import save_user_data

def run_intro():
    questions = get_intro_questions()
    answers = {}

    for q in questions:
        print("AI:", q)
        user_input = input("You: ")
        answers[q] = user_input  # Map Q to A

    # Save the answers
    save_user_data(answers)

if __name__ == "__main__":
    run_intro()
