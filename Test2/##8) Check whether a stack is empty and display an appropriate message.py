##8) Check whether a stack is empty and display an appropriate message

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def Empty(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Stack is not empty!")

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

s.Empty()
    
    
    