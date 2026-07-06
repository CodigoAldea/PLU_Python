# question 14

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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = create_tree()
inorder(root)