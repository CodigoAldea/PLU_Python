# 4. Rank Participants
# A sports academy has recorded the timings (in seconds) of participants in a race.
# Write a program to arrange the timings from the fastest to the slowest so that the winners can be announced


time = [12.5, 13.2, 11.8, 14.1, 12.9]
n = len(time)

for i in range(n):
    mid_index = i
    
    for j in range(i + 1, n):
        if time[j] < time[mid_index]:
            mid_index = j
    time[i], time[mid_index] = time[mid_index], time[i]

print("Participant Timings from Fastest to Slowest:" ,time)
