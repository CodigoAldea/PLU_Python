salary_B1 = [55,65,75,85,95]
salary_B2 =[55,66,77,88,99]
all_salary = salary_B1 + salary_B2
n = len(all_salary)
for i in range(n):
    for j in range(n - i - 1):
        if all_salary[j]  > all_salary[j + 1]:
            all_salary[j], all_salary[j +1 ] = all_salary[j +1], all_salary[j]
print("combined salary: ", all_salary)
