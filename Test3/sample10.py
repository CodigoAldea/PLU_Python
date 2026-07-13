marks = [78, 45, 92, 60, 33, 88, 55, 71, 40, 95,
         67, 82, 29, 74, 58, 91, 36, 63, 85, 49,
         77, 52, 96, 41, 69, 87, 34, 73, 59, 90,
         46, 80, 65, 38, 93, 57, 72, 44, 86, 61,
         31, 79, 54, 98, 66, 43, 89, 62, 35, 75
         ]
n = len(marks)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
            swapped = True
    if not swapped:
        break
    print("Sorted Marks (Ascending):")
    print(marks)
    target = int(input("\nEnter mark to search: "))
    low = 0
    high = n - 1
    found = False
    while low <= high:
        mid = (low + high) //2
    if marks[mid] == target:
        print(f"Mark Found at position {mid + 1} (index {mid})")
        found = True
        break
    elif marks[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Mark Not Found")