# 2) Insert a new node containing 25 after the node containing 20

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

while temp:
    if temp.value == 20:
        new_item = Item(25)
        new_item.next = temp.next
        temp.next = new_item
        break
    temp = temp.next

temp = start

print("After Insertion:")

while temp:
    print(temp.value, end=" ")
    temp = temp.next