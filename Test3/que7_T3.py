scores = [150, 180, 200, 250, 290]

n = len(scores)

for i in range(n - 1):
    for j in range(n - i - 1):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

print("Leaderboard (Highest to Lowest):")
print(scores)