from collections import deque

stack = deque()
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")