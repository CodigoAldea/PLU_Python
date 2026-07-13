class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def count_nodes(self, node):
        if node is None:
            return
        self.count += 1
        self.count_nodes(node.left)
        self.count_nodes(node.right)

BT = BinaryTree()

BT.root = Node(50)
BT.root.left = Node(30)
BT.root.right = Node(70)

BT.count_nodes(BT.root)

print("Total Number of Nodes:", BT.count)