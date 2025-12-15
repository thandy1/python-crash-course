from pathlib import Path
import json

def get_stored_name(path):
    """Get stored information if possible."""
    if path.exists():
        return json.loads(path.read_text())
    else:
        return None

def get_new_username(path):
    """Prompt for a new username and additional info."""
    information = {}
    information['username'] = input("What is your name? ")
    information['age'] = input("How old are you? ")
    information['hobby'] = input("What do you do for fun? ")
    path.write_text(json.dumps(information))    
    return information

def greet_user():
    """Greet user by name."""
    path = Path('chapter-10/remember_me/username4.json')
    information = get_stored_name(path)
    if information:
        verify_user = input(f"Is this the correct username ('y' or 'n'): {information['username']}\n")
        if verify_user.lower() == 'n':
           information = get_new_username(path)
           print(f"We'll remember you when you come back, {information['username']}!")
        else:
            print(f"Welcome back, {information['username']}!")
    else:
        information = get_new_username(path)
        print(f"We'll remember you when you come back, {information['username']}!")

greet_user()

