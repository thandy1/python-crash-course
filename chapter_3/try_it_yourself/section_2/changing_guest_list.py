# 3-5 Changing Guest List:
guests = ["Goku", "Luffy", "Ichigo"]

print(f"Hey {guests[0]}, I'd like to invite you over for dinner.")
print(f"Hey {guests[1]}, you down for some dinner tonight?")
print(f"Hey {guests[2]}, you hungry? Lets try that new burger joint.")

print(f"\nIt seems {guests[0]} cant make it to dinner tonight.\n")

guests[0] = "Naruto"

print(f"Hey {guests[0]}, you available for dinner tonight")
print(f"Hey {guests[1]}, can you still make it to dinner?")
print(f"Hey {guests[2]}, you still down for dinner tonight.")