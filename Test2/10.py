# question 10

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        self.queue.pop(0)

    def display(self):
        for i in self.queue:
            print(i, end=" ")


q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.delete()
q.display()