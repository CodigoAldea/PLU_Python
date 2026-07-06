##7) Display the top element of the stack without removing it

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def check(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        for i in self.stack:
            print(i, end="  ")
        print()

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.display()

s.check()