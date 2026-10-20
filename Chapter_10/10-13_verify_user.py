import json
from pathlib import Path

path = Path("user_profile.json")

def get_stored_username():
    try:
        profile = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return profile.get("username")

def greet_user():
    username = get_stored_username()
    if username:
        answer = input(f"Is this your username, {username}? (y/n) ").strip().lower()
        if answer == "y":
            print(f"Welcome back, {username}!")
            return
    username = input("What is your username? ").strip()
    path.write_text(json.dumps({"username": username}, indent=2), encoding="utf-8")
    print(f"We'll remember you when you come back, {username}!")

greet_user()
