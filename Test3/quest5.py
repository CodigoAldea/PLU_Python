'''5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.'''

book_prices = list(map(int, input("Enter sorted list: ").split()))
new_price = int(input("Enter a new book price: "))

book_prices.append(0)

a = len(book_prices) - 2

while a >= 0 and book_prices[a] > new_price:
    book_prices[a + 1] = book_prices[a]
    a -= 1

book_prices[a + 1] = new_price

print("Updated price list:", book_prices)

