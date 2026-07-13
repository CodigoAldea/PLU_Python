
# 8. Hospital Emergency Queue
# A hospital has a list of patients with different priority levels.
# Write a program to arrange the patients so that the patient with the
# highest priority is treated first.
PRIORITY_LABEL = {
    1: "Critical",
    2: "Serious",
    3: "Moderate",
    4: "Minor"
}

def insertion_sort_by_priority(patients):
    for i in range(1, len(patients)):
        key = patients[i]
        j   = i - 1
        while j >= 0 and patients[j]["priority"] > key["priority"]:
            patients[j + 1] = patients[j]
            j -= 1
        patients[j + 1] = key
    return patients




n = int(input("Enter number of patients: "))
patients = []

for i in range(n):
    print(f"\nPatient {i + 1}:")
    name      = input("  Name: ")
    condition = input("  Condition: ")
    print("  Priority → 1: Critical  2: Serious  3: Moderate  4: Minor")
    priority  = int(input("  Enter priority (1-4): "))

    patients.append({
        "name"     : name,
        "condition": condition,
        "priority" : priority
    })

insertion_sort_by_priority(patients)

print("\n╔══════════════════════════════════════════════════════════╗")
print("║              HOSPITAL EMERGENCY QUEUE                   ║")
print("╠══════════════════════════════════════════════════════════╣")
print(f"║ {'Turn':<5} {'Patient':<15} {'Condition':<18} {'Priority':<12}║")
print("╠══════════════════════════════════════════════════════════╣")
for turn, p in enumerate(patients, start=1):
    label = PRIORITY_LABEL[p["priority"]]
    print(f"║ {turn:<5} {p['name']:<15} {p['condition']:<18} {label:<12}║")
print("╚══════════════════════════════════════════════════════════╝")

print(f"\n→ Treat first: {patients[0]['name']} ({PRIORITY_LABEL[patients[0]['priority']]})")