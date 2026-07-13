'''4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced.'''

timings = list(map(int, input("Enter a time: ").split()))
num = len(timings)

for i in range(num):
    for j in range(num-i-1):
        if timings[j] > timings[j+1]:
            timings[j], timings[j+1] = timings[j+1],timings[j]

print("Fastest to Slowest:",timings)
