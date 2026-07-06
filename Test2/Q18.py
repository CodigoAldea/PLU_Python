graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
def edge(u, v):
    return v in graph.get(u, [])
print(edge('A', 'B'))
print(edge('A', 'D'))