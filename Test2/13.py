# question 13

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

def display(root):
    print(root.data, root.left.data, root.right.data)

root = create_tree()
display(root)