def intro_conversation():
    print("\n👋 Hello! I'm your Career Assistant AI.")
    print("Let's begin by getting to know you a bit.")
    
    name = input("What's your name? ")
    age = input("How old are you? ")
    branch = input("Which engineering branch are you in? ")
    year = input("Which year are you studying? (e.g., 3rd year) ")
    interests = input("What are your interests or favorite tech areas? ")

    # Collect all as a dictionary
    return {
        "name": name,
        "age": age,
        "branch": branch,
        "year": year,
        "interests": interests
    }
