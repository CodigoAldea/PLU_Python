from collections import deque

queue_container = deque()

queue_container.append(10)
queue_container.append(20)
queue_container.append(30)
queue_container.append(40)

print("Queue Elements (FIFO Order):")
while queue_container:
    print(queue_container.popleft(), end=" ")