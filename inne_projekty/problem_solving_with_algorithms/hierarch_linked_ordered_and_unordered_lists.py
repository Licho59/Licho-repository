from node_class import Node
from unordered_complete_linkedList import LinkedList

'''Implementation of hierarchy using unordered linkedlist as superior class. Function 'add' has to be used as below because of ordering mechanism.'''
class OrderedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        #self.head = None

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


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.__str__())
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
