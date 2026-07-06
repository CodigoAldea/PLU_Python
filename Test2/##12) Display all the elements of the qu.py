##12) Display all the elements of the queue in FIFO order

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def display(self):
        for i in self.queue:
            print(i, end="  ")
        print()

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()