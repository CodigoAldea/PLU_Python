# 1) Create a linked list containing the values 10, 20, 30, 40, 50 and display
# all the elements.

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


start = Item(10)
start.next = Item(20)
start.next.next = Item(30)
start.next.next.next = Item(40)
start.next.next.next.next = Item(50)

temp = start

print("Linked List:")

while temp:
    print(temp.value, end=" ")
    temp = temp.next