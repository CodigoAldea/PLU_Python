graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []

def dfs(vertex):
    visited.append(vertex)
    print(vertex, end=" ")

    for i in graph[vertex]:
        if i not in visited:
            dfs(i)

dfs("A")