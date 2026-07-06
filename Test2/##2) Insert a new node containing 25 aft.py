##2) Insert a new node containing 25 after the node containing 20

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def insertAfter(self,target,data):
        current=self.head

        while current is not None:
            if current.data==target:
                newNode=Node(data)
                newNode.next=current.next
                current.next=newNode
                return
            current=current.next

        print("Target value not found!")

    def display(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="  ")
            else:
                print(current.data)
            current = current.next

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insertAfter(20,25)
ll.display()