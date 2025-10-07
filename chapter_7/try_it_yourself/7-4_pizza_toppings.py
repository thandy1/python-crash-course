"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
"""

while True:
    topping_input = input(
        "Enter a topping you would like on your pizza.\n"
        "Type 'quit' when you are done.\n"
        ).strip()
    if topping_input.lower() == "quit":
        break
    else:
        print(f"OK! I'll add {topping_input.title()} to your pizza.")