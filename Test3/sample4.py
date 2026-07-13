sports_timing = [12.5, 13.5, 15.6, 18.8, 11.4]
n =len(sports_timing)
for i in range(n - 1):
    mid_index = i
    for j in range(i +1, n):
        if sports_timing[j] < sports_timing[min_index]:
            min_index = j
            sports_timing[i], sports_timing[min_index] = sports_timing[min_index], sports_timing[i]
            print("race result (fastest to slowest): ")
            for rank in range(n):
                print(f"rank {rank + 1}: {sports_timing[rank]} seconds")
                 
            