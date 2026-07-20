class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited):
        visited.append(vertex)
        print(vertex, end=" ")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


g = Graph()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")

visited = []

print("DFS Traversal:")
g.dfs("A", visited)