book_prices = [15, 20, 25, 30, 40]

new_price = int(input("Enter the new book price: "))

book_prices.append(new_price)

i = len(book_prices) - 2

while i >= 0 and book_prices[i] > new_price:
    book_prices[i + 1] = book_prices[i]
    i -= 1

book_prices[i + 1] = new_price

print("Updated Book Prices:")
print(book_prices)