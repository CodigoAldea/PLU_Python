class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_after(self, value, data):
        current = self.head

        while current is not None:
            if current.data == value:
                new_node = Node(data)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.ref

LL = LinkedList()

LL.insert_start(50)
LL.insert_start(40)
LL.insert_start(30)
LL.insert_start(20)
LL.insert_start(10)

LL.insert_after(20, 25)

LL.display()