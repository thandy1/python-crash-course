# --- List ---
# Collection of items in a particular order (ordered collections)
bicycles = ["trek", "cannondale", "redline", "specialized",]
print(bicycles)

# Accessing Elements in a List
print(bicycles[0]) 
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1])  # cannondale
print(bicycles[3])  # specialized
print(bicycles[-1]) # specialized

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[1].title()}."
print(message)  # My first bicycle was a Cannondale.


# --- Modifying, Adding, and Removing Elements ---
# Modifying Elements in a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)  # [ducati, yamaha, suzuki]

# Adding Elements to a List
motorcycles.append("ducati1")
print(motorcycles)  # Output: [ducati, yamaha, suzuki, ducati1]

# Adding Elements to an empty List
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# Inserting Elements into a List
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)  # Output: [ducati, honda, yamaha, suzuki]

# Removing Elements from a List
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[0]
print(motorcycles)  # Output: [yamaha, suzuki]
del motorcycles[1]
print(motorcycles)  # Output: [yamaha]

# Removing an Item using the pop() Method
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycles = motorcycles.pop()
print(motorcycles)  # Output: [honda, yamaha]
print(popped_motorcycles)   # Output: suzuki

# Popping Items from Any Position in a List
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(motorcycles)  # Output: [yamaha, suzuki] 
print(first_owned)  # Output: honda
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
too_expensive = "honda"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# --- Avoiding Index Errors When Working with Lists ---
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[3])  

