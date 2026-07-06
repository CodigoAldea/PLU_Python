"""##13) Create the following binary tree:
```
50
/ \
30 70
```
Display the root, left child, and right child
    """
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def createTree(self):
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.right = Node(70)

    def display(self):
        print( self.root.data, self.root.left.data, self.root.right.data)

bt = BT()

bt.createTree()

bt.display()