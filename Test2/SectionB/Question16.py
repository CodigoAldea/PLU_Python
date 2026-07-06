class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def leafNodes(self, root):
        if root:
            if root.left is None and root.right is None:
                print(root.data)
            self.leafNodes(root.left)
            self.leafNodes(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)

tree = BinaryTree()

tree.leafNodes(root)