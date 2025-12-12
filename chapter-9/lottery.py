from random import choice

numbers = list(range(1, 11))
letters = ['a', 'b', 'c', 'd', 'e']
pool = numbers + letters

ticket = [choice(pool) for _ in range(4)]

print("Winning ticket:", ticket)