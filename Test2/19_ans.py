from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []
queue = deque()

visited.append("A")
queue.append("A")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for i in graph[vertex]:
        if i not in visited:
            visited.append(i)
            queue.append(i)