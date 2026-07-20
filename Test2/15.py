# question 15

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    return root

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = create_tree()
print(count_nodes(root))