# 10. School Annual Report
# A school has recorded the marks of 50 students.
# Write a program that:
# Sorts the marks in ascending order.
# Accepts a mark from the user.
# Checks whether that mark exists in the sorted list.
# Displays the position if found; otherwise, prints "Mark Not Found."


marks = [56,78,90,45,66,89,70,81,55,60]

n = len(marks)

for i in range(n):

    for j in range(n-i-1):

        if marks[j] > marks[j+1]:

            marks[j], marks[j+1] = marks[j+1], marks[j]

print("Sorted Marks:", marks)

target = int(input("Enter Mark to Search: "))

low = 0

high = len(marks)-1

found = False

while low <= high:

    mid = (low+high)//2

    if marks[mid] == target:

        print("Mark Found at Position:", mid)

        found = True

        break

    elif target < marks[mid]:

        high = mid-1

    else:

        low = mid+1

if not found:

    print("Mark Not Found")