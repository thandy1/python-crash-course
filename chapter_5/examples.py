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