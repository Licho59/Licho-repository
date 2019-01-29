'''Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.'''

class QueueADT:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, value):
        return self.items.append(value)
        
    def dequeue(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
