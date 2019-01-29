from node_class import Node

class OrderedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        current = self.head
        linkedList = []
        while current != None:
            linkedList.append(current.getData())
            current = current.getNext()
        return linkedList
        
    def isEmpty(self):
        return self.head == None
        
    def popPos(self, key):
        if self.isEmpty():
            print("The list is empty!")
            return False
        current = self.head
        previous = None
        count = 0
        found = False
        while not found:
            if count == key:
                found = True
                break
            else:
                previous = current
                current = current.getNext()
                count += 1
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
        return current.getData()
        
    def pop(self):
        if self.head.next == None:
            temp = self.head
            self.head.data = None
            return temp
        current = self.head
        previous = None
        while current.next != None:
            previous = current
            current = current.next
        previous.next = current.next
        return current.data
        
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def remove(self, data):
        if self.isEmpty():
            print("List is EMPTY!")
            return None
        current = self.head
        previous = None
        while current != None:
            if current.getData() != data:
                previous = current
                current = current.getNext()
            else:
                temp = current
                previous.setNext(current.next)
                current = previous.getNext()
                return temp.data
        print("The number " + str(data) + " has not been found in the list")
        return False
        
        
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
print(mylist.__str__())
print(mylist.popPos(2))
print(mylist.pop())
print(mylist.size())
print(mylist.remove(77))
print(mylist.remove(29))
print(mylist.__str__())
print(mylist.size())
