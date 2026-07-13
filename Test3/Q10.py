marks = [78, 56, 89, 45, 92, 67, 34, 88, 90, 71, 60, 82, 55, 73, 99]
n = len(marks)

for i in range(n):
    for j in range(0, n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j] 

print("Sorted Marks:", marks)

input = int(input("Enter the mark to search for: "))

position = -1
for i in range(n):
    if marks[i] == input:
        position = i + 1  
        break             


print(f"Mark Found! Position: {position}" if position != -1 else "Mark Not Found.")