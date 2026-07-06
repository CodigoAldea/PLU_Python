from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

removed = queue.popleft()
print("Removed element:", removed)
print("Updated Queue:", list(queue))