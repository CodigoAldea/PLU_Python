# question 7

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        print(self.stack[-1])


s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.peek()