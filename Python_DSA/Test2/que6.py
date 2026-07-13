
from collections import deque
stack_container = deque()
stack_container.append(5)
stack_container.append(10)
stack_container.append(15)
stack_container.append(20)
print("Stack Container:", stack_container)
stack_container.pop()
print("updated stack:", stack_container)