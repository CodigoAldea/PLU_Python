class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)

tree = BinaryTree()

tree.inorder(root)