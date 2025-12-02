print("The Deli has run out of Pastrami.\n")

sandwich_orders = [
    "Ham & Cheese",
    "Grilled Cheese",
    "pastrami",
    "Club Sandwich",
    "pastrami",
    "BLT",
    "pastrami",
    ] 

finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

# Test
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
