graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
def has_edge(u, v):
    return v in graph.get(u, [])
print(has_edge('A', 'B'))
print(has_edge('A', 'D'))