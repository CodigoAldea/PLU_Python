class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        self.queue.pop(0)

    def display(self):
        print(self.queue)

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.delete()

q.display()