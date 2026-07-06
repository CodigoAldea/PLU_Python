class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            self.stack.pop()

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            for i in self.stack:
                print(i)


s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

print("Original Stack:")
s.display()

s.pop()

print("\nUpdated Stack:")
s.display()