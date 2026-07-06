# 3) Delete the node containing 30 from the linked list and display the updated
# list

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

while temp.next:
    if temp.next.value == 30:
        temp.next = temp.next.next
        break
    temp = temp.next

temp = start

print("After Deletion:")

while temp:
    print(temp.value, end=" ")
    temp = temp.next