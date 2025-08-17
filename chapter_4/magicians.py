# --- Looping Through an Entire List ---
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, thats was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, thats was a great trick!")
    print(f"I cant wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")


