# --- Making Numerical Lists ---
# Using the range() function
for value in range(1, 5):
    print(value)   

# Using range() to Make a List of Numbers
numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # Output: 0
print(max(digits))  # Output: 9
print(sum(digits))  # Output: 45

# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]