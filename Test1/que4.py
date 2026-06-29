def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 10):
        print(i, "*", num, "=", i * num)    