'''6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.'''


employee_salary1 = list(map(int, input("Enter branch salary 1 : ").split()))
employee_salary2 = list(map(int, input("Enter branch salary 2 : ").split()))

Salary = employee_salary1+employee_salary2
Salary.sort()

print("Ascending Salary:", Salary)
