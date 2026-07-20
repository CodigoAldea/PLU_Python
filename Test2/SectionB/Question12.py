class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def display(self):
        for i in self.queue:
            print(i)


q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.display()