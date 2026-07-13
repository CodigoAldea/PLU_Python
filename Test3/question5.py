
# 5. Insert New Book by Price
# A bookstore maintains a sorted list of book prices.
# A new book arrives, and its price needs to be placed at the correct
# position while keeping the list sorted.
# Write a program to perform this task.
def insert_into_sorted(prices, new_price):
    prices.append(0)                        
    i = len(prices) - 2                    

    while i >= 0 and prices[i] > new_price:
        prices[i + 1] = prices[i]          
        i -= 1

    prices[i + 1] = new_price             



n = int(input("Enter number of existing books: "))

prices = []
print("Enter prices in ascending order:")
for i in range(n):
    p = float(input(f"  Book {i + 1} price: ₹"))
    prices.append(p)

print(f"\nCurrent price list: {prices}")

new_price = float(input("\nEnter price of new book: ₹"))

insert_into_sorted(prices, new_price)

print(f"Updated price list:  {prices}")

 

