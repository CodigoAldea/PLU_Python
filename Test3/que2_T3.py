product_ids = [10, 15, 18, 20, 25, 28, 30]

search = int(input("Enter Product ID to search: "))

low = 0
high = len(product_ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if product_ids[mid] == search:
        print("Product Found at index:", mid)
        found = True
        break

    elif product_ids[mid] < search:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Product Not Available")
    