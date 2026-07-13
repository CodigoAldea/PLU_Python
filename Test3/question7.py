# 7. Online Game Leaderboard
# An online gaming platform stores players' scores.
# Write a program to arrange the scores in descending order so that the
# leaderboard can be displayed.
def insertion_sort_desc(scores):
    for i in range(i,len(scores)):
        key = scores[i]
        j = i - 1

        while j >= 0 and scores[j] < key:
            scores[j + i] = scores[j]
            j -=1
        scores[j + 1] = key 
    return scores 
n = int (input("Enter number of players:"))

players = []
scores = []
for  i  in range(n):
    name  = input(f"\nEnter name of player {i + 1}: ")
    score = int(input(f"Enter score of {name}: "))
    players.append(name)
    scores.append(score)


combined = list(zip(scores, players))
print("\n╔══════════════════════════════════╗")
print("║        GAME LEADERBOARD         ║")
print("╠══════════════════════════════════╣")
print(f"║ {'Rank':<5} {'Player':<15} {'Score':<8}║")
print("╠══════════════════════════════════╣")
for rank, (score, name) in enumerate(combined, start=1):
    print(f"║ {rank:<5} {name:<15} {score:<8}║")
print("╚══════════════════════════════════╝")
    