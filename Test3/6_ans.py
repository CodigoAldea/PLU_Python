# 6. Employee Salary Report
# An HR department has employee salary records collected from two different branches.
# Write a program to combine both lists and display all salaries in ascending order.

salaries_branch1 = [55050, 60010, 60040, 80000]
salaries_branch2 = [55000, 65000, 75000, 85000]


combined_salaries = salaries_branch1 + salaries_branch2

n = len(combined_salaries)
for i in range(n):
    for j in range(n - i - 1):
        if combined_salaries[j] > combined_salaries[j + 1]:
            combined_salaries[j], combined_salaries[j + 1] = combined_salaries[j + 1], combined_salaries[j]

print("Combined Employee Salaries in Ascending Order: ",combined_salaries)

