# 6) Employee Salary Report
# An HR department has employee salary records collected from two different
# branches.
# Write a program to combine both lists and display all salaries in
# ascending order

a = list(map(int, input("Enter first salary list: ").split()))
b = list(map(int, input("Enter second salary list: ").split()))

pay = a + b

n = len(pay)

for i in range(n):
    for j in range(n-i-1):
        if pay[j] > pay[j+1]:
            pay[j], pay[j+1] = pay[j+1], pay[j]

print("Ascending Order:")
print(pay)