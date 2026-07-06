class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  

    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

my_stack = Stack()

node_5 = Node(20)
node_5.next = my_stack.top
my_stack.top = node_5

node_10 = Node(15)
node_10.next = my_stack.top
my_stack.top = node_10

node_15 = Node(10)
node_15.next = my_stack.top
my_stack.top = node_15

node_20 = Node(5)
node_20.next = my_stack.top
my_stack.top = node_20

my_stack.display()