# 4) Count and display the total number of nodes in the linked list

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


start = Item(10)
start.next = Item(20)
start.next.next = Item(30)
start.next.next.next = Item(40)
start.next.next.next.next = Item(50)

count = 0
temp = start

while temp:
    count += 1
    temp = temp.next

print("Total Nodes =", count)