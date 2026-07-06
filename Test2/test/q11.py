class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def front(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Front Element =", self.queue[0])

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

print("Queue Elements:")
q.display()

print("\nFront Element:")
q.front()