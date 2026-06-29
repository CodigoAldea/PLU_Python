try:
    a = int(input("Enter first number: "))
    b = int(input("Enter secound number: "))
    print(a/b)
except ZeroDivisionError: 
    print("can not divide by zero")