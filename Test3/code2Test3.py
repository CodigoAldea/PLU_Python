# 2) Product ID Search
# An e-commerce website stores product IDs in ascending order.
# Write a program to find whether a customer-entered product ID exists in
# the inventory. If it exists, display its index; otherwise, display "Product
# Not Available

m = int(input("Enter number of products: "))
pid = []
for i in range(m):
    pid.append(int(input("Enter Product ID: ")))
x = int(input("Enter Product ID to Search: "))
first = 0
last = m - 1
while first <= last:

    mid = (first + last) // 2

    if pid[mid] == x:
        print("Product Available at Index:", mid)
        break

    elif x < pid[mid]:
        last = mid - 1

    else:
        first = mid + 1
else:
    print("Product Not Available")