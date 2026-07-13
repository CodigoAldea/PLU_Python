# 6. Employee Salary Report
# An HR department has employee salary records collected from two different
# branches.
# Write a program to combine both lists and display all salaries in
# ascending order.


salary1 = [25000, 30000, 40000]
salary2 = [28000, 35000, 45000]
salary = salary1 + salary2
salary.sort()
print("Sorted Salaries:", salary)