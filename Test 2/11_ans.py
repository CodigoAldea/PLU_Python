from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Front element:", queue[0])
print("Queue:", list(queue))