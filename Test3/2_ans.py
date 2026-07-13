# 2. Product ID Search
# An e-commerce website stores product IDs in ascending order.
# Write a program to find whether a customer-entered product ID exists in
# the inventory. If it exists, display its index; otherwise, display "Product
# Not Available."

product_ids = [10, 12, 13, 14, 15, 16,18]
search_id = int(input("Enter the product ID to search: "))
low = 0
high = len(product_ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if product_ids[mid] == search_id:
        found = True
        print(f"Product Found at index: {mid}")
        break
    elif product_ids[mid] < search_id:
        low = mid + 1
    else:
        high = mid - 1
        
if not found:
    print("Product Not Available.")