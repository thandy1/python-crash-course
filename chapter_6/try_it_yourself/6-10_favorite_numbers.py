"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favorite_numbers = {
    "mary": [5, 2, 6],
    "james": [10, 12],
    "chris": [7, 3],
    "mike": [9, 6, 3],
    "jack": [2, 4],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
