from core.conversation.intro_conversation import intro_conversation
from core.save_user import save_user_data

# Start the intro Q&A
user_data = intro_conversation()

# Save the data
save_user_data(user_data)

print("\n✅ Your responses have been saved. Thank you!")
