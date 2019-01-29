from node_class import Node

class UnorderedList:
    '''Completed with additional methods like append, index, insert and pop. Additinally updated with currect monitoring the length of the list. The algorithm is O(n) performance because of not introduced 'tail' element.'''

    def __init__(self):
        self.head = None
        self.length  = 0
    
    def __str__(self):
        list_content = []
        current = self.head
        while current != None:
            list_content.append(str(current.getData()))
            current = current.getNext()
        print(list_content)
        return "The list contains: " + ','.join(list_content) # int __str_ string has to be returned!
        
    def isEmpty(self):
        return self.length == 0

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1

    def size(self):
        return self.length
        
 
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
        try:
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
            self.length -= 1
        except:
            print("Number", item, "not found in the list!")
            
    def append(self, item):
        current = self.head
        found = False
        temp = Node(item)
        while current != None and not found:
            if current.getNext() == None:
                current.setNext(temp)
                found = True                
            else:
                current = current.getNext()
        self.length += 1
    
    def index(self, num):
        current = self.head
        count = 0
        while current != None:
            if current.getData() == num:
                return count
            else:
                count += 1
                current = current.getNext()
                
    def insert(self, item, place):
        current = self.head
        count = 0
        while current != None:
            if place == 0:
                temp = Node(item)
                temp.setNext(self.head)
                self.head = temp
                break          
            elif count == place - 1:
                temp = Node(item)
                temp.setNext(current.getNext())
                current.setNext(temp)                   
                break
            else:
                current = current.getNext()
                count += 1
        self.length += 1
                
    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
        self.length -= 1
        return current
        
    def slice(self, start, stop):
        current = self.head
        sliced_part = []
        count = 0
        while current.getNext() != None and count < stop:
            if count == start:
                sliced_part.append(current.getData())
                count += 1
                while count < stop:
                    current = current.getNext()
                    sliced_part.append(current.getData())
                    count += 1
            else:
                current = current.getNext()
                count += 1
        return sliced_part
                
            
mylist = UnorderedList()

mylist.add(31)
mylist.append(400)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.insert(55, 0)
mylist.pop()
mylist.remove(200)
mylist.add(17)

print(mylist.size())
print(mylist.__str__())
print(mylist.search(400))
print(mylist.slice(2,4))
print(mylist.index(31))
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
