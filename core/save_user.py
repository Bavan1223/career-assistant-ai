import json
import os
from datetime import datetime

def save_user_data(user_data: dict):
    """Save user data to a uniquely named JSON file."""
    folder_path = "data/user_profiles"
    os.makedirs(folder_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"user_data_{timestamp}.json"
    filepath = os.path.join(folder_path, filename)

    with open(filepath, "w") as f:
        json.dump(user_data, f, indent=4)
