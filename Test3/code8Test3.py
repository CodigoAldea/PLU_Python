# 8. Hospital Emergency Queue
# A hospital has a list of patients with different priority levels.
# Write a program to arrange the patients so that the patient with the
# highest priority is treated first.

n = int(input("Enter number of patients: "))

priority = []

for i in range(n):
    priority.append(int(input("Enter Priority: ")))

for i in range(n):
    for j in range(n-i-1):
        if priority[j] < priority[j+1]:
            priority[j], priority[j+1] = priority[j+1], priority[j]

print("Emergency Queue:")
print(priority)