def binary_search(array, target):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2 
        
        if array[mid] == target:
            return mid  
        
        elif array[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return -1  


def main():
    products = []  
    
    print("Enter Product IDs in ascending order (type 'done' to stop):")
    while True:
        item = input()
        if item.lower() == 'done': 
            break
       
        products.append(int(item)) 

    if not products: 
        return print("Inventory is empty.")

    target_id = int(input("Enter Product ID to search: "))
    
    index = binary_search(products, target_id)
    
    if index != -1:
        print(f"Product found at index: {index}")
    else:
        print("Product Not Available.")

main()