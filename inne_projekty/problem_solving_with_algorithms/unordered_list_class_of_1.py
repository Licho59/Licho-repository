from node_class import Node

class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail == None:
            self.tail = temp
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self, item):
        temp = Node(item)
        self.tail.setNext(temp)
        self.tail = temp


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.remove(77)
print(mylist.size())
mylist.append(150)
mylist.remove(31)
mylist.append(200)
mylist.remove(17)
mylist.append(144)
mylist.remove(144)
print(mylist.search(144))
print(mylist.size())
