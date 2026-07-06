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

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.ref
        print("Total number of nodes:", count)

    def display(self):
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
print()
LL.count_nodes()