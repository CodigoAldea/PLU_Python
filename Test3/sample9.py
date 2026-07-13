id = [1001, 1005, 1012, 1020, 1035, 1048, 1050, 1067, 1080, 1099]
target = int(input("enter a book id: "))
low = 0
high = len(id) - 1
found = False 
comparision = 0
while low <= high:
    mid = (low +  high) //2
    comparision +=1
    if id[mid] == target:
        print(f"book found at index {mid} (position {mid + 1})")
        found = True
        break
    elif id[mid] < target:
        low = mid +1 
    else:
        high = mid - 1
        if not found:
            print("book nt found in library")
            print(f"total comparision: {comparision}")