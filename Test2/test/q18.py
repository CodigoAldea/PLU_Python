class Graph:
    def __init__(self):
        self.graph = {}

    def generate(self, data):
        self.graph[data] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def hasPath(self, start, end):
        if end in self.graph[start]:
            print("Path Exists")
        else:
            print("Path Does Not Exist")


graph = Graph()

graph.generate('A')
graph.generate('B')
graph.generate('C')
graph.generate('D')

graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('B', 'D')
graph.addEdge('C', 'D')

graph.hasPath('A', 'D')