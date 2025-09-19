favorite_numbers = {
    "mary": 5,
    "james": 10,
    "chris": 7,
    "mike": 9,
    "jack": 2,
}

print("Mary's favorite number is", favorite_numbers["mary"])
print("James's favorite number is", favorite_numbers["james"])
print("Chris's favorite number is", favorite_numbers["chris"])
print("Mike's favorite number is", favorite_numbers["mike"])
print("Jack's favorite number is", favorite_numbers["jack"])

name = input("Enter your name: ")
favorite_numbers[name] = int(input("Enter your favorite number: "))
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}")
