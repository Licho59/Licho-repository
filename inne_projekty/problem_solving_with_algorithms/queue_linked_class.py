class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    '''That implementation for Queue class has O(1) performance both for enqueue and dequeue operations.'''
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def isEmpty(self):
        pass
        return self.length == 0

    def size(self):
        return self.length

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.back = self.front
        else:
            self.back.next = node
            self.back = node
        self.length += 1
        
    def dequeue(self):
        if self.isEmpty():
            return 'The list is EMPTY!'
        else:
            node = self.front
            self.front = self.back
            self. back = self.back.next
            self.length -= 1
        return node.data
        
    def prt(self):
        if not self.isEmpty():
            node = self.front
            while node != None:
                print(node.data, end='-> ')
                node = node.next
            return 'null'
        else:
            print('Queue is Empty!')

if __name__ == '__main__':        
    myqueue = Queue()
    myqueue.enqueue(10)
    myqueue.enqueue(20)
    myqueue.enqueue(30)
    print(myqueue.size())
    print(myqueue.prt())      
    print(myqueue.dequeue())
    print(myqueue.size())        
