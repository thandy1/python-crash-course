dream_vacation = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could go anywhere in the world, where would you go? ")
    dream_vacation[name] = response
    repeat = input("Would you like to enter another location? (y/n): ")
    if repeat.lower() == "n":
        break
    else:
        continue
    
print("\nResults:")
for name, vacation in dream_vacation.items():
    print(f"{name.title()} wants to go to {vacation.title()}.")