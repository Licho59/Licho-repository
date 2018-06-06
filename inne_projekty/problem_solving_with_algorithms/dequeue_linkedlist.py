class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
    def __str__(self):
        deq_list = []
        current = self.head
        while current != None:
            deq_list.append(current.data)
            current = current.next
        return deq_list
        
    def addFront(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail == None:
            self.tail = self.head
        self.length += 1
        return str(self.head.data) + ' is now the first element of the list.'
        
    def removeFront(self):
        if self.tail == None:
            return 'The list is EMPTY!'
        elif self.tail == self.head:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = self.head.next
        self.length -= 1
        return str(node.data) + ' - the first element of the list has just been removed!'
    
    def addRear(self, data):
        node = Node(data)     
        if self.tail == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
        self.length += 1
        return str(self.tail.data) + ' - it is the last element of the list.'
        
    def removeRear(self):
        if self.length == 0:
            return 'The list is EMPTY!'
        current = self.head
        previous = None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return 'The list has been emptied just now!'
        else:
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            self.length -= 1
            return str(current.data) + ' has been removed from the list.'
            
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return 'False - the list is NOT EMPTY!'
        
    def __len__(self):
        return self.length
            
        
         
        
mydequeue = Dequeue()
print(mydequeue.addFront(10))
print(mydequeue.isEmpty())
print(mydequeue.removeRear())
print(mydequeue.__str__())
print(mydequeue.addFront(20))
print(mydequeue.__str__())
print(mydequeue.removeFront())
print(mydequeue.__str__())
print(mydequeue.addRear(30))
print(mydequeue.addFront(40))
print(mydequeue.__len__())
print(mydequeue.__str__())
print(mydequeue.removeRear())
print(mydequeue.__str__())
