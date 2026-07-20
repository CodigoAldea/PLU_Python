class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)

print_leaf_nodes(root)