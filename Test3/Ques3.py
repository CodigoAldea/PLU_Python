# 3. Arrange Exam Marks
# A teacher wants to display students' marks from the lowest to the
# highest.
# Write a program to sort the marks of all students in ascending order.

Marks = [50, 36, 64, 99, 89, 75]
n = len(Marks)
for i in range (n):
    for j in range (n-i-1):
        if Marks[j] > Marks[j + 1]:
            Marks[j], Marks[j + 1] = Marks[j + 1], Marks[j]
            print("Sorted Marks: ", Marks)