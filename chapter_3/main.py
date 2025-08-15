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
print(motorcycles)  # ducati, yamaha, suzuki

