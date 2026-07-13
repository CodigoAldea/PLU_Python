patients = [2, 5, 1, 4, 3]   

n = len(patients)

for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if patients[j] > patients[max_index]:
            max_index = j

    patients[i], patients[max_index] = patients[max_index], patients[i]

print("Patients arranged by priority:")
print(patients)