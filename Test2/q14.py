# 14) Perform an Inorder Traversal on a binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

print("Inorder Traversal:")
inorder(root)