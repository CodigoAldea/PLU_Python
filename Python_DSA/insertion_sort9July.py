var = [7, 3, 5, 12, 2, 9]

# Traverse from the second element
for i in range(1, len(var)):

    # Step 1 & 2: Read and hold the current element
    current = var[i]

    # Compare with previous elements
    j = i - 1

    # Step 3 & 4: Compare and shift
    while j >= 0 and var[j] > current:
        var[j + 1] = var[j]   # Shift element to the right
        j -= 1

    # Insert the held element at the correct position
    var[j + 1] = current

print("Sorted List:", var)

