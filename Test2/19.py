# question 19

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []
queue = []

visited.append("A")
queue.append("A")

print("BFS Traversal:")

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            queue.append(i)