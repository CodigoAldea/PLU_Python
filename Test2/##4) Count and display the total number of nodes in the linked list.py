##4) Count and display the total number of nodes in the linked list
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
        
    def remove(self,value):
        current=self.head
        if current is not None and current.data == value:
            self.head = current.next
            return

        while current is not None and current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        print("Target value not found!")
        
    def countNodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

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
ll.remove(30)
ll.display()
print("Total number of nodes:", ll.countNodes())
    