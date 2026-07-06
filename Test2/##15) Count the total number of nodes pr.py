##15) Count the total number of nodes present in a binary tree

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

    def countNodes(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)

bt = BinaryTree()

bt.createTree()

print("Total number of nodes:", bt.countNodes(bt.root))