class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_after(self, target_value, new_value):
        current = self.head
        while current is not None:
            if current.data == target_value:
                break
            current = current.next
        if current is None:
            print(f"Node with value {target_value} not found in the list.")
            return
        new_node = Node(new_value)
        
        new_node.next = current.next
   
        current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(10)
    second = Node(20)
    third = Node(30)
    
    ll.head.next = second
    second.next = third

    print("Original List:")
    ll.print_list()

    print("\nInserting 25 after 20...")
    ll.insert_after(20, 25)

    print("\nUpdated List:")
    ll.print_list()