def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

def main():
    timings = []
    
    print("Enter race timings in seconds (type 'done' to stop):")
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        timings.append(float(entry))

    if not timings:
        return print("No timings were recorded.")

    print("\nRecorded Timings:", timings)
    selection_sort(timings)
    
    print("\n--- Final Rankings (Fastest to Slowest) ---")
    for rank, time in enumerate(timings):
        print(f"Rank {rank + 1}: {time} seconds")

main()
