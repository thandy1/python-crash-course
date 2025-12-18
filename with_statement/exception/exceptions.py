filename = "extra/with_statement/count.txt"
# Read existing count
try:
    with open(filename, 'r') as file:
        count = int(file.read())
except FileNotFoundError:
    count = 0

# Each program execution increments the counter
count += 1

# Save updated count
with open(filename, 'w') as file:
    file.write(str(count))

print(f"Program has been run {count} times.")

