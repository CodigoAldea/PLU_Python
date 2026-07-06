##14) Perform an Inorder Traversal on a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def createTree(self):
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.right = Node(70)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

bt = BinaryTree()

bt.createTree()

print("Inorder Traversal:")
bt.inorder(bt.root)