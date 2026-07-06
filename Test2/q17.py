# 17.Create an undirected graph with the following edges: Display the adjacency list of the graph
# * A – B
# * A – C
# * B – D
# * C – D

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("Adjacency List:")

for node in graph:
    print(node, "->", graph[node])