sandwich_orders = [
    "Ham & Cheese",
    "Grilled Cheese",
    "Club Sandwich",
    "BLT",
    ] 

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("\n\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich}")

# Test to see if sandwich_orders is empty
# print(sandwich_orders)