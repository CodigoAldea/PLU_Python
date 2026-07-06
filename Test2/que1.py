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
    def display(self):
        if self.head is None:
            current = self.head
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
LL.display()