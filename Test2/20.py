# question 20

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for i in graph[node]:
            dfs(i)

print("DFS Traversal:")
dfs("A")