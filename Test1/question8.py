# Handle division by zero using try and except.
try:
   a = int(input("Enter the number: "))
   b = int(input("Enter the second number: "))
   print(a/b)
except ZeroDivisionError:
   print("Cannot divide by zero")