queue = []

def add_patient(name, priority):
    queue.append((priority, name))
    
    i = len(queue) - 1
    while i > 0 and queue[i][0] > queue[i - 1][0]:
        queue[i], queue[i - 1] = queue[i - 1], queue[i] 
        i -= 1
    print(f"Added: {name} (Priority {priority})")

add_patient("John (Flu)", 2)
add_patient("Sarah (Heart Attack)", 5)  
add_patient("Mike (Broken Arm)", 3)

print("\nSorted Queue (Highest Priority First):", queue)

if queue:
    treated = queue.pop(0)  
    print(f"\n NOW TREATING: {treated[1]} with Priority {treated[0]}")

add_patient("Alex (Severe Burn)", 4)

print("\nUpdated Queue:", queue)