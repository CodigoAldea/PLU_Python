# 5) Insert New Book by Price
# A bookstore maintains a sorted list of book prices.
# A new book arrives, and its price needs to be placed at the correct
# position while keeping the list sorted.
# Write a program to perform this task. 

book = list(map(int, input("Enter sorted prices: ").split()))

p = int(input("Enter new price: "))

book.append(p)

for i in range(1, len(book)):
    temp = book[i]
    j = i - 1

    while j >= 0 and book[j] > temp:
        book[j+1] = book[j]
        j = j - 1

    book[j+1] = temp

print(book)