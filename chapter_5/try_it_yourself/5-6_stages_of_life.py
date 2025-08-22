age = 22

if age < 2:
    person = "baby"
elif 2 <= age < 4:
    person = "toddler"
elif 4 <= age < 13:
    person = "kid"
elif 13 <= age < 20:
    person = "teenager"
elif 20 <= age < 65:
    person = "adult"
else: 
    person = "elder"

print(f"This person is a(n) {person.title()}.")