# 5. Insert New Book by Price
# A bookstore maintains a sorted list of book prices.
# A new book arrives, and its price needs to be placed at the correct position while keeping the list sorted.
# Write a program to perform this task

book_prices = [15.99, 25.50, 35.00, 45.25, 55.75]
new_price = float(input("Enter the price of the new book: "))
book_prices.append(new_price)

i = len(book_prices) - 2

while i >= 0 and book_prices[i] > new_price:
    book_prices[i + 1] = book_prices[i]
    i -= 1

book_prices[i + 1] = new_price

print("Updated Book Prices in Ascending Order:", book_prices)