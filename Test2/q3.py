class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
head = Node(10)
head.next = Node(20)
head.next.next = Node(25)
head.next.next.next = Node(30)
print("Original List:")
print_list(head)
curr = head
while curr and curr.next:
    if curr.next.data == 30:
        curr.next = curr.next.next  # Bypass the node containing 30
        break
    curr = curr.next
print("\nUpdated List (After deleting 30):")
print_list(head)