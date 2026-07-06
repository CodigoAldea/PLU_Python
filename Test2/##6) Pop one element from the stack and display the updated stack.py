##6) Pop one element from the stack and display the updated stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Popped element:", self.stack.pop())

    def display(self):
        for i in self.stack:
            print(i, end="  ")
        print()

a = Stack()

a.push(5)
a.push(10)
a.push(15)
a.push(20)
a.pop()
a.display()