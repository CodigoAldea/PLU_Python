'''use bubble sort to sort [10,9,100,20,5]
# list = [10,9,100,20,5]
# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
print(list)'''


'''# sort the dictionary by values
data = {10: 'asdf', 2: 'asdf', 5: 'asdf',8: 'asdf'}

# Sort by key (ascending)
sorted_by_key = dict(sorted(data.items()))
print(sorted_by_key)
# Output: {2: 'asdf', 5: 'asdf', 8: 'asdf', 10: 'asdf'}

# Sort by value (ascending)
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_value)
# Output: {2: 'asdf', 8: 'asdf', 5: 'asdf', 10: 'asdf'}'''

'''#sort the dictionary by values
var_items = [('A',1),('B',5),('C',3),('D',4)]
sorted_items = sorted(var_items, key=lambda x: x[1])
print(sorted_items)'''

'''A cricket coach has the scores of 15 players.

Requirements
	Accept scores of all players.
	Display the original list.
	Sort the scores using Bubble sort.
	Display the sorted scores.
	Ask the coach to enter a player's score.
	search for the score using Binary search.
	Display the player's rank based on the sorted list.
	Also Display: 
		Highest score
		Lowest score
		Total number of players
'''
# Cricket coach score program
# This program accepts 15 player scores, sorts them using Bubble Sort,
# searches for a score using Binary Search, and shows useful information.

scores = []

print("Enter scores of 15 players:")
for i in range(15):
    score = int(input(f"Enter score of player {i + 1}: "))
    scores.append(score)

print("\nOriginal scores:", scores)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


sorted_scores = bubble_sort(scores.copy())
print("\nSorted scores (ascending):", sorted_scores)

search_score = int(input("\nEnter a player's score to search: "))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


position = binary_search(sorted_scores, search_score)

if position != -1:
    rank = len(sorted_scores) - position
    print(f"\nScore {search_score} found at position {position + 1} in the sorted list.")
    print(f"Rank of the player: {rank}")
else:
    print("\nScore not found.")

print("\nHighest score:", sorted_scores[-1])
print("Lowest score:", sorted_scores[0])
print("Total number of players:", len(scores))
