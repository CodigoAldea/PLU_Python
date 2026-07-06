a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
    print(a/b)
except:
    print("Divisible by Zero is not possible")
finally:
    print("code Excueted")