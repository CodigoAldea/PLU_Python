class Queue:
    def __init__(self):
        self.queue = []
    def insert(self, data):
        self.queue.append(data)
    def display(self):
        print(self.queue)
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.display()