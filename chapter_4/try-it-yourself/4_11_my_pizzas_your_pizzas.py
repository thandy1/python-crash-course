# 4-11 My Pizzas, Your Pizzas:
my_pizzas = ["sausage", "pepperoni", "cheese"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("bacon")
friend_pizzas.append("french")

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza) 