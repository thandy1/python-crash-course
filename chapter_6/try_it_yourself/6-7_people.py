people = []

person_0 = {
    "first": "John",
    "last": "Doe",
    "age": 999,
    "city": "Gotham",
    }

person_1 = {
    "first": "Ben",
    "last": "Bone",
    "age": 99,
    "city": "New York",
    }

person_2 = {
    "first": "Sarah",
    "last": "Cruz",
    "age": 23,
    "city": "Dallas"
}

people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:
    full_name = f"{person['first']} {person['last']}"
    age = person["age"]
    city = person["city"]
    print(
        f"Name: {full_name}"
        f"\nAge: {age}"
        f"\nCity: {city}\n"
        )
