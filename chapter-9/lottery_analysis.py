from random import choice
my_ticket = [1, 'a', 3, 'b']
pool = list(range(4)) + ['a', 'b']

attempt = 0
while True:
    # Periodic prints to track progress
    if attempt % 1000 == 0:
        print(f"Attempt {attempt} so far...")
    attempt += 1

    # Generates an empty list each iteration when false match
    sample_ticket = []

    # Picks a value from the pool and appends it to the empty list
    for _ in range(len(my_ticket)):
        sample_ticket.append(choice(pool))
    if sample_ticket == my_ticket:
        print(
            f"Attempts: {attempt}\n"
            f"Winning ticket: {my_ticket}\n"
            f"Sample ticket: {sample_ticket}\n"
            )
        break
        