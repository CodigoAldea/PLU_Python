'''7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.'''

player_score = list(map(int, input("Enter a scores: ").split()))
sco = len(player_score)

for i in range(sco):
    for j in range(sco-i-1):
        if player_score[j] < player_score[j+1]:
            player_score[j], player_score[j+1] = player_score[j+1], player_score[j]

print("leaderboard:", player_score)

