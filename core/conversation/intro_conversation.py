def intro_conversation():
    print("\n👋 Hello! I'm your Career Assistant AI.")
    print("Let's start by getting to know you a bit. Please answer the following questions:\n")

    name = input("🧑 What’s your name? ")
    age = input("📅 How old are you? ")
    branch = input("📘 Which engineering branch are you in? (e.g., CSE, ECE, ME) ")
    year = input("🎓 What year are you studying in? (e.g., 2nd year, 3rd year) ")
    interests = input("💡 What are your tech interests or favorite areas? (e.g., AI, Web Dev, App Dev, etc.) ")

    print("\n✅ Thanks for sharing! Let’s move ahead...\n")

    # Collect responses as a dictionary
    return {
        "name": name.strip().title(),
        "age": age.strip(),
        "branch": branch.strip().upper(),
        "year": year.strip(),
        "interests": interests.strip()
    }
