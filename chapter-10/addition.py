try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid. Please enter a number.")
else:
    print(num1 + num2)