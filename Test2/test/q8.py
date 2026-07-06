class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")


s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.isEmpty()