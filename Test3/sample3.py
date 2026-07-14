marks = [78, 45, 92, 69, 33, 88]
n = len(marks)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
            swapped = True
            if not swapped:
                break
            print("marks ascending order: ", marks)
        