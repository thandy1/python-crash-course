"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""


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
