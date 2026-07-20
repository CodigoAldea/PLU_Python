class Graph:
    def __init__(self):
        self.graph = {}

    def generate(self, data):
        self.graph[data] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])


graph = Graph()

graph.generate('A')
graph.generate('B')
graph.generate('C')
graph.generate('D')

graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('B', 'D')
graph.addEdge('C', 'D')

print("Adjacency List:")
graph.display()