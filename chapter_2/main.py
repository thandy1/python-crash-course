# --- Naming and using variables ---
# Variables are labels or Values are assigned to variables
greeting_message = "Hello There"
print(greeting_message)

message_1 = "Hi"
print(message_1)

mesage = "Hello Python Crash Course reader!"
print(mesage)


# --- Strings ---
# Changing case in a string with methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!!"
print(message)

# Adding whitespace to strings with tabs or newlines 
print("Languages: \n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace
favorite_language = "python "
print(favorite_language.rstrip())

language = " python"
language = language.lstrip()
print(language)

language_2 = " JavaScript "
print(language_2.strip())

# Removing prefixes
nostartch_url = "https://nostartch.com"
print(nostartch_url.removeprefix("https://"))
simple_url = nostartch_url.removeprefix("https://")
print(simple_url)

# Avoiding syntax errors with strings
text = "One of Python's strengths is it's diverse community."
print(text)
# text = 'One of Python's strengths is it'ts diverse community.'


# --- Numbers ---
# Integers
a = 2 + 3   # -, *, /, %, **, //
print(a)

# Floats
b = 0.5 + 0.2   # -, *, /, %, **, //
print(b)

# Integers and Floats
print(4 / 2)    # Output: 2.0 (Float-pointing division)
print(4 // 2)   # Output: 2 (Floor division)

d = 1 + 2.0
print(d)    # Output: 3.0

# Underscores in Numbers
universe_age = 14_000_000
print(universe_age)     # Output: 14000000
print(14000000)     # Output: 14000000

# Multiple Assignment
x, y, z = 0, 0, 0
print(x, y, z)      # Output: 0 0 0

# Constants
# Python does not support constant variables, this is a social contract in python, not a safety net.
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)


# --- Comments ---
"""
Can also be used to comment since python ignores strings not assigned to a variable.
"""

