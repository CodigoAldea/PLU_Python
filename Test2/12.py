# question 12

class Queue:
    def __init__(self):
        self.queue = [10, 20, 30, 40]

    def show(self):
        for i in self.queue:
            print(i, end=" ")


q = Queue()
q.show()