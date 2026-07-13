# 18.Check whether there is a direct edge between two given vertices

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

first = input("Enter first vertex: ")
second = input("Enter second vertex: ")

if second in graph[first]:
    print("Direct Edge Exists")
else:
    print("No Direct Edge")