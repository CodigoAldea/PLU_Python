class Stack:
    def __init__(self):
        self.stack = []
    def insert(self, data):
        self.stack.append(data)
    def top(self):
        print("Top Element:", self.stack[-1])
s = Stack()
s.insert(5)
s.insert(10)
s.insert(15)
s.insert(20)
s.top()