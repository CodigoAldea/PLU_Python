list = [  ["dexmo", 3],["Sneha", 5],["Amit", 1],["Priya", 4],["Karan", 2]]
n = len(list)
for i in range(n - 1):
     max_index = i
     for j in range(i + 1, n):
         if list[j][1] > list[max_index][1]:
             max_index = j
             list[i], list[max_index] = list[max_index], list[i]
             print("HOSPITAL EMERGENCY QUEUE")
             print("-" * 30)
             for pos in range(n):
                 print(f"{pos + 1}. {list[pos][0]}  (Priority: {list[pos][1]})")