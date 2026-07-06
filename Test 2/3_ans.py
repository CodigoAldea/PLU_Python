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
        while current:
            if current.data == value:
                new_node = Node(data)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref

    def delete_node(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.ref
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.ref

        if current is None:
            print("Node not found")
            return

        prev.ref = current.ref

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.ref


a = LinkedList()
a.insert_start(50)
a.insert_start(40)
a.insert_start(30)
a.insert_start(20)
a.insert_start(10)

a.insert_after(20, 25)

a.delete_node(30)

print("Updated Linked List:")
a.display()