'''8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.
'''

priority_levels = list(map(int, input("Enter patient priority levels: ").split()))

for i in range(1, len(priority_levels)):
    key = priority_levels[i]
    j = i - 1

    while j >= 0 and priority_levels[j] < key:
        priority_levels[j + 1] = priority_levels[j]
        j -= 1

    priority_levels[j + 1] = key

print("Patients arranged by highest priority:")
print(priority_levels)