class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
        else:
            current = self.head

            while current.ref is not None:
                current = current.ref

            current.ref = NewNode

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.ref


ll = LinkedList()

ll.insertNode(10)
ll.insertNode(20)
ll.insertNode(30)
ll.insertNode(40)
ll.insertNode(50)

print("Linked List:")
ll.display()