'''2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available.'''

Invent = list(map(int, input("Enter product IDs in ascending order: ").split()))
product_id = int(input("Enter product id to search: "))

Found = False
for i in range(len(Invent)):
    if Invent[i] == product_id:
        print("Product found at Index:", i)
        found = True
        break
if not found:
    print("Product Not Available")
