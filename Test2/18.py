# question 18

def create_graph():
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['B', 'C']
    return graph

def check_edge(graph, u, v):
    if v in graph[u]:
        print("Edge exists")
    else:
        print("Edge does not exist")

g = create_graph()
check_edge(g, 'A', 'B')