##11) Display the front element of the queue without removing it
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def display(self):
        for i in self.queue:
            print(i, end="  ")
        print()
    def check(self):
        if len(self.queue) == 0:
            print("queue is empty!")
        else:
            print("front element:", self.queue[-1])
    
    def pop(self):
        if len(self.queue) == 0:
            print("queue is empty!")
        else:
            print("removed element:", self.queue.pop())

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()
q.check()
