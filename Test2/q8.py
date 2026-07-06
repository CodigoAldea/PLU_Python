class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")