GLOBAL_DICT = {}

class Graph:
    def add_edge(self, node1, node2):
        if node1 not in GLOBAL_DICT:
            GLOBAL_DICT[node1] = []
        if node2 not in GLOBAL_DICT:
            GLOBAL_DICT[node2] = []

        GLOBAL_DICT[node1].append(node2)
        GLOBAL_DICT[node2].append(node1)

    def display(self):
        for node in GLOBAL_DICT:
            print(node, "->", GLOBAL_DICT[node])

G = Graph()

G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")

print("Adjacency List:")
G.display()