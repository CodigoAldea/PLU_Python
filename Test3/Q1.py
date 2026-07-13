def linear_search(array, target):
   
    for i in range(len(array)):
        if array[i] == target:
            return i + 1  
    return -1


def main():
    roll_numbers = []  
    
    print("Enter roll numbers (type 'done' to stop):")
    while True:
        roll = input()
        if roll.lower() == 'done': break
        roll_numbers.append(roll) 

    if not roll_numbers: return print("List is empty.")

    target = input("Enter roll number to search: ")
    position = linear_search(roll_numbers, target)
    
    print(f"Student Found at position: {position}") if position != -1 else print("Student Not Found.")

main()