"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pet_1 = {'animal': 'dog', 'owner': 'Ben',}
pet_2 = {'animal': 'cat', 'owner': 'Sarah',}
pet_3 = {'animal': 'turtle', 'owner': 'Mike',}
pet_4 = {'animal': 'hamster', 'owner': 'Lily',}

pets = []

# .extend() method to append multiple entries to a list
pets.extend([pet_1, pet_2, pet_3, pet_4])
for pet in pets:
    print(f"{pet['owner']} has a {pet['animal'].title()}.")
