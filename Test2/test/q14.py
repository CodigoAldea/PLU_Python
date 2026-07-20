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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


tree = BST()

tree.insertNode(50)
tree.insertNode(30)
tree.insertNode(70)

print("Inorder Traversal:")
tree.inorder(tree.root)