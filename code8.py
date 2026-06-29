# Handle division by zero using try and except.

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print(x / y)

except ZeroDivisionError:
    print("Cannot divide by zero")