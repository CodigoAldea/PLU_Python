class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)

tree = BinaryTree()

print("Total Nodes:", tree.count(root))
