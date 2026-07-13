student_marks =[30,40,50,60,70]

n = len(student_marks)

for i in range(n - 1):
    for j in range(n - i - 1):
        if student_marks[j] > student_marks[j + 1]:
            student_marks[j], student_marks[j + 1] = student_marks[j + 1], student_marks[j]

print("Marks in Ascending Order:")
print(student_marks)