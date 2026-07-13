def bubble_sort(array):
    
    n = len(array)
    
    for i in range(n):
       
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    marks = []  
    
    print("Enter student marks one by one (type 'done' to stop):")
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        marks.append(float(entry))

    if not marks:
        return print("No marks were entered.")

    print("\nOriginal Marks:", marks)
    
    bubble_sort(marks)
    
    print("Sorted Marks (Lowest to Highest):", marks)


main()