class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def display(self):
        print(self.stack)
s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.display()