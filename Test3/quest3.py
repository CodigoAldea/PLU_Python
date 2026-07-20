'''3. Arrange Exam Marks
A teacher wants to display students' marks from the lowest to the
highest.
Write a program to sort the marks of all students in ascending order.'''


marks = list(map(int, input("Enter the marks: ").split()))
num = len(marks)

for i in range(num):
    for j in range(num - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Ascending Order:", marks)
