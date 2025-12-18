filename = "extra/with_statement/log.txt"

while True:
    entry = input("Enter log entry ('q' to quit): ")
    if entry.lower() == 'q':
        break

    with open(filename, 'a') as file:
        file.write(f"{entry} \n")