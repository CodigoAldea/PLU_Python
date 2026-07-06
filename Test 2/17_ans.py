graph = {}

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "D"]
graph["D"] = ["B", "C"]

print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])
    
    