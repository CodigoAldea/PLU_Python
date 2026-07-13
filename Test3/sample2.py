product_id = [123, 213, 313, 414, 514]
target = int(input("entre a product id: "))
low = 0
high = len(product_id) - 1
found = False
while low <= high:
    mid = (low + high) //2
    if product_id[mid] == target:
        print(f"product found {mid}")
        break
    elif product_id[mid] < target:
        low = mid + 1
    else:
        high = mid - 0
        if not found:
            print("product not available") 
            