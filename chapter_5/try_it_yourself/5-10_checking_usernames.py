current_users = ["Ben", "Batman", "Spiderman", "Mary", "Ironman"]

current_users_lower = [user.lower() for user in current_users]

new_users = ["Ben", "Johnny", "Mary", "Chris", "Bella"]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} already in use. Enter new username.")
    else:
        print(f"{new_user} is available.")

    
