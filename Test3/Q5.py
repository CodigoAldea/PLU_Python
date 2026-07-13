def insert_in_sorted_order(array, new_price):
    array.append(new_price)
    
    i = len(array) - 2
    while i >= 0 and array[i] > new_price:
        array[i + 1] = array[i]
        i -= 1
        
    array[i + 1] = new_price

def main():
    book_prices = []
    
    print("Enter current book prices in sorted order (type 'done' to stop):")
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        book_prices.append(float(entry))

    if not book_prices:
        return print("The inventory is empty.")

    new_book_price = float(input("Enter the price of the new book: "))
    
    print("\nOriginal Prices:", book_prices)
    
    insert_in_sorted_order(book_prices, new_book_price)
    
    print("Updated Prices (Still Sorted):", book_prices)

main()
