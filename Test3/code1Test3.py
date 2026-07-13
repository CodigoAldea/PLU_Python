# 1) Student Roll Number Search
# A teacher has stored the roll numbers of students in a list in the order
# they registered. The list is not sorted.
# Write a program to check whether a given roll number exists in the list.
# If found, display its position; otherwise, print "Student Not Found."

n = int(input("Enter number of students: "))

roll = []

for i in range(n):
    roll.append(int(input("Enter Roll Number: ")))

search = int(input("Enter Roll Number to Search: "))

for i in range(n):
    if roll[i] == search:
        print("Student Found at Position:", i)
        break
else:
    print("Student Not Found")