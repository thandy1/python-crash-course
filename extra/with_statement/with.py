filename = "extra/with_statement/message.txt"

# Write to the file
with open(filename, 'w') as file:
    message = input("Enter a message: ")
    file.write(message)

# Read from the file
with open(filename, 'r') as file:
    contents = file.read()

print("File contents:")
print(contents)
# File is automatically closed each time