# question 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_after_20(self, data):
        temp = self.head
        while temp:
            if temp.data == 20:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


l = LinkedList()

l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.insert_end(40)
l.insert_end(50)

l.insert_after_20(25)
l.display()