#The linked list implementation is called a singly linked list because each node has a single reference to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation, each node has a reference to the next node(commonly called next) as well as a reference to the preceding node(commonly called back). The head reference also contains two references, one to the first node in the linked list and one to the last. Code this implementation in Python.


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def size(self):
        return self.size
        
    def __str__(self):
        dblist = []
        if self.size == 0:
            return "The list is EMPTY!!"
            
        current = self.head
        while current.next_node != self.head:
            dblist.append(current.data)
            current = current.next_node
        if current == self.last:
            dblist.append(current.data)
        return dblist
        
    def search(self, item):
        if self.size == 0:
            print("List EMPTY - nothing to search")
        current = self.head
        count = 0
        while count <= self.size:
            if current.data == item:
                return "The item " + str(item) + " has been found!"
            else:
                count += 1
                current = current.next_node
        return "The item " + str(item) + " has not been found"
            
    def add(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.last = self.head
            self.last.next_node = self.head.prev_node
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.last.next_node = new_node
            self.head = new_node
        self.size += 1

    def remove(self, item):
        if self.size == 0:
            print("There is nothing to remove when the list is EMPTY!")
        elif self.size == 1:
            if self.head.data == item:
                self.head = None
                self.size -= 1
                return "The element of the list " + str(item) + " has just been removed. The list is EMPTY now!"
        else:
            current = self.head
            while current.next_node != self.head:
                if current.data == item:
                    if current == self.head:
                        self.head = current.next_node
                        self.last.next_node = self.head
                    else:
                        temp = current.prev_node
                        temp.next_node = current.next_node
                    self.size -= 1
                    return "The element of the list " + str(item) + " has just been removed."
                else:
                    current = current.next_node
            if current == self.last:
                if current.data == item:
                    self.last = current.prev_node
                    self.last.next_node = self.head.prev_node
                    current = None
                    self.size -= 1
                    return "The element of the list " + str(item) + " has just been removed."
                        
            return "There is no such an element as " + str(item) + " on the list!"
            
    
                
d_linked = DoublyLinkedList()

d_linked.add(10)
d_linked.remove(10)
print(d_linked.__str__())
d_linked.add(20)
print(d_linked.size)
d_linked.add(30)
print(d_linked.remove(10))
d_linked.add(40)
print(d_linked.size)
print(d_linked.remove(50))
print(d_linked.remove(40))
print(d_linked.__str__())
print(d_linked.search(30))
print(d_linked.search(20))
print(d_linked.search(200))
print(d_linked.search(40))
print(d_linked.__str__())
