class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def display(self):
        print(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)

stack.pop()
stack.display()