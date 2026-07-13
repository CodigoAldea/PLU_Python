# 7) Online Game Leaderboard
# An online gaming platform stores players' scores.
# Write a program to arrange the scores in descending order so that the
# leaderboard can be displayed.

n = int(input("Enter number of players: "))

score = []

for i in range(n):
    score.append(int(input("Enter Score: ")))

for i in range(n):
    for j in range(n-i-1):
        if score[j] < score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]

print("Leaderboard:")
print(score)