# --- Working with Part of a List ---
# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:5])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[0:5:2])

# Looping through a Slice
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
