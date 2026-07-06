class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is None:
        return

    inorder_traversal(node.left)

    print(node.data, end=" ")

    inorder_traversal(node.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)

inorder_traversal(root)
print()  
