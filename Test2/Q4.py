class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

my_list.display()

count = 0  
current = my_list.head  

while current is not None:
    count += 1 
    current = current.next  

print("Total no of nodes:", count)