# 4. Rank Participants
# A sports academy has recorded the timings (in seconds) of participants in
# a race.
# Write a program to arrange the timings from the fastest to the slowest so
# that the winners can be announced.

timings = [30, 20, 15, 25, 40]
n = len(timings)
for i in range (n):
    for j in range(n-i-1):
        if timings[j] > timings[j + 1]:
            timings[j], timings[j + 1] = timings[j + 1], timings[j]
            print("Ranked Timings: ", timings)