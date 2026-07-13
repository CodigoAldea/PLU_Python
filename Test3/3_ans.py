# 3. Arrange Exam Marks
# A teacher wants to display students' marks from the lowest to the highest.
# Write a program to sort the marks of all students in ascending order

marks = [85, 92, 78, 96, 88]

n = len(marks)

for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Marks in ascending order:")
print(*marks)