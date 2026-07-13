class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

BT = BinaryTree()

BT.root = Node(50)
BT.root.left = Node(30)
BT.root.right = Node(70)

print("Inorder Traversal:")
BT.inorder(BT.root)