favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

# List of people who should take the poll
fav_lang_poll = ["jen", "phil", "sarah", "micah", "laura"]

for person in fav_lang_poll:
    if person in favorite_languages:
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"{person.title()}, you should take the poll.")