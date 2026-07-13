# 1. Student Roll Number Search
# A teacher has stored the roll numbers of students in a list in the order
# they registered. The list is not sorted.
# Write a program to check whether a given roll number exists in the list.
# If found, display its position; otherwise, print "Student Not Found."

roll_num=[1,2,3,4,5,6]
roll_search=int(input("Enter the roll number to search: "))
if roll_search in roll_num: 
    print(f"Student Found at position: {roll_num.index(roll_search)}")
else:
    print("Student Not Found.")