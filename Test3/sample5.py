newbook_price = [200, 199, 188, 256, 198, 391, 300]
new_price = input(input("enter a new book price: "))
newbook_price.append(new_price)
i = len(new_price) - 2
key = new_price
while i >=0 and new_price[i] > key:
    newbook_price[i + 1] = newbook_price[i]
    i -=1
    newbook_price[i + 1] = key
    print("update sorted book list", newbook_price)