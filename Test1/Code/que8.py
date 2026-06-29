# Handle division by zero using try and except.

try:
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))

    print("Result: ", a / b)

except:
    print("Error") 