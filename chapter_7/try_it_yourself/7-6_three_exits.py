"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value
"""

active = True
while active:
    age = input(
        "How old are you?\n"
        "Type 'quit' when you are finished.\n"
        )
    if age.lower() == "quit":
        active = False
        continue

    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.") 
    else:
        print("Your ticket costs $15.") 