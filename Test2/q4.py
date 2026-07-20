class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(25)
count = 0
curr = head
while curr:
    count += 1
    curr = curr.next
print(count)