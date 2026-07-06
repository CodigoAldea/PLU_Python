class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def leaf_nodes(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.data, end=" ")
        self.leaf_nodes(node.left)
        self.leaf_nodes(node.right)
BT = BinaryTree()

BT.root = Node(50)
BT.root.left = Node(30)
BT.root.right = Node(70)
BT.root.left.left = Node(20)
BT.root.left.right = Node(40)
BT.root.right.left = Node(60)
BT.root.right.right = Node(80)

print("Leaf Nodes:")
BT.leaf_nodes(BT.root)