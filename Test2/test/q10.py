class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            self.queue.pop(0)

    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            for i in self.queue:
                print(i)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Original Queue:")
q.display()

q.dequeue()

print("\nUpdated Queue:")
q.display()
