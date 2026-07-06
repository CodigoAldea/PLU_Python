# 16) Find and display all the leaf nodes of a binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def show_leaf(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.value)

    show_leaf(node.left)
    show_leaf(node.right)


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Leaf Nodes:")
show_leaf(root)