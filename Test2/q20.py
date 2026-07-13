# 20.Perform a Depth-First Search (DFS) traversal starting from vertex A.

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for next_node in graph[node]:
            dfs(next_node)

dfs("A")