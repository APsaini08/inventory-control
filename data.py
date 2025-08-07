import os
import json

def load_data(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)
    
    with open(file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def checkuserid(user_id, file):
    data = load_data(file)
    return any(account.get("id") == user_id for account in data)
