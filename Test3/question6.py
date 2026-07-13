# 6. Employee Salary Report
# An HR department has employee salary records collected from two different
# branches.
# Write a program to combine both lists and display all salaries in
# ascending order.
def merge_sorted(branch_a, branch_b):
    merged = []
    i = 0 
    j = 0 
    while i < len(branch_a) and j < len(branch_b):
        if branch_a[i] <= branch_b[j]:
            merged.append(branch_a[i])
            i += 1 
        else:
            merged.append(branch_b[j])
            j += 1

    while i < len(branch_a):
        merged.append(branch_a[i])
        i += 1 
    while j < len(branch_b):
        merged.append(branch_b[j])
        j += 1
    return merged
def input_sorted_salaries(branch_name):
    n = int(input(f"\nEnter number of employees in {branch_name}: "))
    salaries = []
    print(f"Enter salaries of {branch_name} in ascending order:")
    for i in range(n):
        s = float(input(f"Employee {i + 1}: "))
        salaries.append(s)
    return salaries
branch_a = input_sorted_salaries("Branch A")
branch_b = input_sorted_salaries("Branch B")

combined = merge_sorted(branch_a, branch_b)

print(f"Branch A  ({len(branch_a)} employees): {branch_a}")
print(f"Branch B  ({len(branch_b)} employees): {branch_b}")
print(f"\nCombined  ({len(combined)} employees): {combined}")
print(f"\nLowest salary : ₹{combined[0]}")
print(f"Highest salary: ₹{combined[-1]}")

