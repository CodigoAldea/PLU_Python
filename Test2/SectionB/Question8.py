class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")
s = Stack()
s.isEmpty()