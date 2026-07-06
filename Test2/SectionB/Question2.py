class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def insertAfter(self, value, data):
        current = self.head
        while current is not None:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
        print("None")
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insertAfter(20, 25)
ll.display()