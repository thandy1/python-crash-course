from pathlib import Path
import json

def get_stored_name(path):
    """Get stored username if possible."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

# Change the path to the file that exists
def greet_user():
    """Greet user by name."""
    path = Path('chapter-10/remember_me/username3.json')
    username = get_stored_name(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
