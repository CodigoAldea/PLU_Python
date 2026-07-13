def merge_sorted_lists(branch1, branch2):
    combined = []
    i = 0
    j = 0
    
    while i < len(branch1) and j < len(branch2):
        if branch1[i] < branch2[j]:
            combined.append(branch1[i])
            i += 1
        else:
            combined.append(branch2[j])
            j += 1
            
    while i < len(branch1):
        combined.append(branch1[i])
        i += 1
        
    while j < len(branch2):
        combined.append(branch2[j])
        j += 1
        
    return combined

def main():
    branch_A = []
    branch_B = []
    
    print("Enter sorted salaries for Branch A (type 'done' to stop):")
    while True:
        entry = input()
        if entry.lower() == 'done': break
        branch_A.append(float(entry))
        
    print("\nEnter sorted salaries for Branch B (type 'done' to stop):")
    while True:
        entry = input()
        if entry.lower() == 'done': break
        branch_B.append(float(entry))

    print("\nBranch A Salaries:", branch_A)
    print("Branch B Salaries:", branch_B)
    
    sorted_report = merge_sorted_lists(branch_A, branch_B)
    
    print("\nCombined Salary Report (Sorted):", sorted_report)

main()