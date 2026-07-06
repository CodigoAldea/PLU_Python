class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def display(self):
        print(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print(stack.peek())