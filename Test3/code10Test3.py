# 10) School Annual Report
# A school has recorded the marks of 50 students.
# Write a program that:
# Sorts the marks in ascending order.
# Accepts a mark from the user.
# Checks whether that mark exists in the sorted list.
# Displays the position if found; otherwise, prints "Mark Not Found

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    marks.append(int(input("Enter Marks: ")))

for i in range(n):
    for j in range(n-i-1):
        if marks[j] > marks[j+1]:
            marks[j], marks[j+1] = marks[j+1], marks[j]

print("Sorted Marks:")
print(marks)

x = int(input("Enter mark to search: "))

for i in range(n):
    if marks[i] == x:
        print("Mark Found at Position:", i)
        break
else:
    print("Mark Not Found")



 
 
 