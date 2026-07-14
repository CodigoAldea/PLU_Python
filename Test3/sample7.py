scores = [450, 1200, 800, 300, 950]
n = len(scores)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]
            swapped = True
    if not swapped:
        break
print("LEADERBOARD")
for rank in range(n):
    print(f"Rank {rank + 1}: {scores[rank]} points")