graph = {}

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "D"]
graph["D"] = ["B", "C"]

print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])

v1 = input("Enter first vertex: ")
v2 = input("Enter second vertex: ")

if v2 in graph[v1]:
    print("Direct edge exists.")
else:
    print("Direct edge does not exist.")