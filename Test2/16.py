# question 16

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inertNode(self, data):
        NewNode = Node(data)
        if self.root is None:
            self.root = NewNode
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = NewNode
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = NewNode
                        break
                    else:
                        current = current.right

    def leafNodes(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        self.leafNodes(root.left)
        self.leafNodes(root.right)

tree = BinaryTree()
tree.inertNode(50)
tree.inertNode(30)
tree.inertNode(70)

print("Leaf nodes of the binary tree:")
tree.leafNodes(tree.root)