# 8. Hospital Emergency Queue
# A hospital has a list of patients with different priority levels.
# Write a program to arrange the patients so that the patient with the
# highest priority is treated first.

patients = [1,4,2,5,3]  
n = len(patients)

for i in range(n-1):
    mid_index = i
    for j in range(i + 1, n):
        if patients[j] > patients[mid_index]:
            mid_index = j
    patients[i], patients[mid_index] = patients[mid_index], patients[i]

print("Patients arranged by priority:", patients)