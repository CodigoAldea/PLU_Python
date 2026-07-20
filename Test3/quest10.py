'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found.'''

grades = list(map(int, input("Enter student marks: ").split()))

count = len(grades)

for pass_no in range(count - 1):
    for check in range(count - pass_no - 1):
        if grades[check] > grades[check + 1]:
            grades[check], grades[check + 1] = grades[check + 1], grades[check]

print("Sorted Marks:", grades)

required_mark = int(input("Enter mark to search: "))

first = 0
last = len(grades) - 1
result = False

while first <= last:
    guess = (first + last) // 2

    if grades[guess] == required_mark:
        print("Mark found at position:", guess)
        result = True
        break
    elif grades[guess] < required_mark:
        first = guess + 1
    else:
        last = guess - 1

if result == False:
    print("Mark Not Found")