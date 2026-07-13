# 19) Perform a Breadth-First Search (BFS) traversal starting from vertex A

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

queue = []
visited = []

start = "A"

queue.append(start)
visited.append(start)

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for next_node in graph[node]:
        if next_node not in visited:
            visited.append(next_node)
            queue.append(next_node)