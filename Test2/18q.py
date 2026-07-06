
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


v1 = "A"
v2 = "B"

if v2 in graph[v1]:
    print("Direct edge exists")
else:
    print("Direct edge does not exist")