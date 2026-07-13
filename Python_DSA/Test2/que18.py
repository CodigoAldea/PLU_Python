GLOBAL_DICT = {}

class Structure:
    def add_edge(self, node1, node2):
        if node1 not in GLOBAL_DICT:
            GLOBAL_DICT[node1] = []
        GLOBAL_DICT[node1].append(node2)

    def check_edge(self, node1, node2):
        if node1 in GLOBAL_DICT and node2 in GLOBAL_DICT[node1]:
            print("Direct edge exists")
        else:
            print("Direct edge does not exist")

G = Structure()

G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")

print(GLOBAL_DICT)

G.check_edge("A", "C")