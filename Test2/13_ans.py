class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

BT = BinaryTree()

BT.root = Node(50)
BT.root.left = Node(30)
BT.root.right = Node(70)

print("Root:", BT.root.data)
print("Left Child:", BT.root.left.data)
print("Right Child:", BT.root.right.data)