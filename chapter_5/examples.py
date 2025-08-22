# Checking Whether a Value is in a List
requested_toppings = ["mushrooms", "onions", "pineapple"]

if "mushrooms" in requested_toppings:
    print("Yes")
else:
    print("No")

# Checking Whether a Value is Not in a List
banned_users = ["andrew", "carolina", "david"] 
user = "marie"

if user not in banned_users:
    print(f"{user.title()} is not in banned users list.")

# Testing Multiple Conditions
requested_toppings = ["mushrooms", "extra_cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")
if "extra_cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

