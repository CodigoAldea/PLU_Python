# 7. Online Game Leaderboard
# An online gaming platform stores players' scores.
# Write a program to arrange the scores in descending order so that the
# leaderboard can be displayed.


scores = [450, 780, 320, 910, 650]
n = len(scores)
for i in range(n):
    for j in range(n-i-1):
        if scores[j] < scores[j+1]:
            scores[j], scores[j+1] = scores[j+1], scores[j]
print("Leaderboard:", scores)