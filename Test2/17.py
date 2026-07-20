# question 17

def create_graph():
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['B', 'C']
    return graph

def display(graph):
    for i in graph:
        print(i, ":", graph[i])

g = create_graph()
display(g)