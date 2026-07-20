# 2. Product ID Search
# An e-commerce website stores product IDs in ascending order.
# Write a program to find whether a customer-entered product ID exists in
# the inventory. If it exists, display its index; otherwise, display "Product
# Not Available."

Product_ID = [102, 110, 100, 105, 150]
target = int(input("Enter Product ID: "))
low = 0
high = len(Product_ID) - 1
while low <= high:
    mid = (low + high) // 2
    if Product_ID[mid ] == target:
        print("Product Found at Index: ", mid)
        break
    elif target < Product_ID[mid]:
        high = mid -1
    else: 
        low = mid + 1
else:
    print("Product Not Available")