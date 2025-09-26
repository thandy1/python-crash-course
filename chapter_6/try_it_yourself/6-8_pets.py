pet_1 = {'animal': 'dog', 'owner': 'Ben',}
pet_2 = {'animal': 'cat', 'owner': 'Sarah',}
pet_3 = {'animal': 'turtle', 'owner': 'Mike',}
pet_4 = {'animal': 'hamster', 'owner': 'Lily',}

pets = []

# .extend() method to append multiple entries to a list
pets.extend([pet_1, pet_2, pet_3, pet_4])
for pet in pets:
    print(f"{pet['owner']} has a {pet['animal'].title()}.")
