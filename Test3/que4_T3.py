timings = [15.8, 12.5, 14.2, 11.9, 13.6]

n = len(timings)

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if timings[j] < timings[min_index]:
            min_index = j

    timings[i], timings[min_index] = timings[min_index], timings[i]

print("Timings from Fastest to Slowest:")
print(timings)