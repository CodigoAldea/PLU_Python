# 4) Rank Participants
# A sports academy has recorded the timings (in seconds) of participants in
# a race.
# Write a program to arrange the timings from the fastest to the slowest so
# that the winners can be announced.

m = int(input("Enter number of participants: "))

sec = []

for i in range(m):
    sec.append(int(input("Enter Time: ")))

for i in range(m):
    for j in range(m-i-1):
        if sec[j] > sec[j+1]:
            sec[j], sec[j+1] = sec[j+1], sec[j]

print("Fastest to Slowest:")
print(sec)