print(sorted(cities, reverse=True))

cities.sort(reverse=True)
print(cities)

cities.append("Houston")
print(cities)

removed = cities.pop(1)
print(cities)

print(len(cities))

del cities[2]
print(cities)

cities.insert(1, "Las Vegas")
print( cities)

cities.remove("Dallas")
print(cities)