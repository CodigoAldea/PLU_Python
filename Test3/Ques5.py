# 5. Insert New Book by Price
# A bookstore maintains a sorted list of book prices.
# A new book arrives, and its price needs to be placed at the correct
# position while keeping the list sorted.
# Write a program to perform this task.


Prices = [420, 360, 450, 490, 330]
new_price = int(input("Enter New Book Price: "))
Prices.append(new_price)
for i in range(1, len(Prices)):
    key = Prices[i]
    j = i - 1
    while j >= 0 and Prices[j] > key:
        Prices[j + 1] = Prices[j]
        j-=1
        Prices[j + 1] = key
        print("Updated Price List: ", Prices)