class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertNode(self, data):
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

    def countNodes(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


tree = BST()

tree.insertNode(50)
tree.insertNode(30)
tree.insertNode(70)

count = tree.countNodes(tree.root)

print("Total Nodes =", count)