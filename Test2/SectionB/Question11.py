class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def front(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Front Element:", self.queue[0])


q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.front()