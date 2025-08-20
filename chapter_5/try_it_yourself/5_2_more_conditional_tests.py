car = "Subaru"
print(car != "subaru")
print(car == "subaru")

car_2 = "Audi"
print(f"\n{car_2.lower() == 'audi'}")

num = 2
print(f"\n{num > 1}")
print(f"{num >= 1}")
print(f"{num <= 1}")
print(f"{num != 1}")
print(f"{num == 1}")

fruit = "apple"
print(f"\n{fruit == 'orange' or fruit == 'apple'}")
print(f"{fruit != 'banana' and fruit != 'strawberry'}")

items = ["pencil", "notebook", "backpack", "eraser"]
if "pencil" in items:
    print(f"\nTrue")

print("marker" not in items)