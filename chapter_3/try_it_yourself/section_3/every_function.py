# 3-10 Every Function:
cities = ["Dallas", "New York", "Austin", "Los Angeles"]

cities.sort()
print(cities)

cities.reverse()
print(cities)

print(sorted(cities))

print(sorted(cities, reverse=True))

cities.sort(reverse=True)
print(cities)

cities.append("Houston")
print(cities)

print(cities.pop(1))

print(len(cities))

del cities[2]
print(cities)

cities.insert(1, "Las Vegas")
print( cities)

cities.remove("Dallas")
print(cities)