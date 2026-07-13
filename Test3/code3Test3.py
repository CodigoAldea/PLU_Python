# 3) Arrange Exam Marks
# A teacher wants to display students' marks from the lowest to the
# highest.
# Write a program to sort the marks of all students in ascending order. 

m = int(input("Enter number of students: "))
mark = []
for i in range(m):
    mark.append(int(input("Enter Marks: ")))
for i in range(m):
    for j in range(m-i-1):
        if mark[j] > mark[j+1]:
            mark[j], mark[j+1] = mark[j+1], mark[j]
print("Ascending Order:")
print(mark)