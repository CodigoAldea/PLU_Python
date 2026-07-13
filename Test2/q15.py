# 15) Count the total number of nodes present in a binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_nodes(node):
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

total = count_nodes(root)

print("Total Nodes:", total)