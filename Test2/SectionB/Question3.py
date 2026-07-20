class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
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

ll.delete(30)

ll.display()