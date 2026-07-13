# 13.Create the following binary tree Display the root, left child, and right child :
# 50
# / \
# 30 70

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(50)

root.left = TreeNode(30)
root.right = TreeNode(70)

print("Root Node:", root.value)
print("Left Child:", root.left.value)
print("Right Child:", root.right.value)