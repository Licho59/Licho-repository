import timeit

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        
    def printQueue(self):
        return self.items
        
myqueue = Queue()
for i in range(1000):
    myqueue.enqueue(i)

    