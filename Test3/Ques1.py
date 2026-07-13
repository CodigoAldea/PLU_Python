# 1. Student Roll Number Search
# A teacher has stored the roll numbers of students in a list in the order
# they registered. The list is not sorted.
# Write a program to check whether a given roll number exists in the list.
# If found, display its position; otherwise, print "Student Not Found."


Roll_Numbers = [59, 54, 60, 20, 67]
Roll = int(input("Enter Roll Number: "))
found = False
for i in range(len(Roll_Numbers)):
    if Roll_Numbers[i] == Roll:
        print("Student Found at Position:", i)
        found = True
        break
if not found:
    print("Student Not Found")