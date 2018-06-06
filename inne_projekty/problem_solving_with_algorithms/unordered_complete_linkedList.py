from node_class import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
        self.tail = self.head
        self.length += 1
        
        '''
        def size(self): # alternative method for counting size of list
        current = self.head
        count = 0
        while not (current is None):
            count += 1
            current = current.getNext()
        return count
        '''

    def remove(self, data):
        current = self.head
        prev = None
        found = False

        try:
            while not found:
                if current.getData() == data:
                    found = True
                else:
                    prev = current
                    current = current.getNext()
            if prev is None:
                self.head = current.getNext()
            else:
                prev.setNext(current.getNext())
            self.length -= 1
        except AttributeError:
            print("The number " + str(data) +
                  " can not be removed because there is no such number in the list.")

    def slice(self, start, stop):
        """ return a copy of the list starting at start position
        and going upto but not including stop position """
        if (start < 0) or (start > stop) or (stop > self.length + 1):
            print("Invalid range.")
            return None
        stop = stop - 1
        curr = self.head
        count = 0
        while curr is not None:
            if count == start:
                break
            curr = curr.next
            count += 1
        node = Node(curr.data)
        front = node
        back = front
        while count < stop:
            curr = curr.next
            node = Node(curr.data)
            back.next = node
            back = back.next
            count += 1

        curr = front
        result = []
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        print("Sliced list: ")
        print(result)

        #return front

    def pop(self, i=-1):
        """ Remove the item at the given position in the linked list,
        and return it.
        If no index is specified, a.pop() removes and returns the last item
        in the linked list."""
        if self.isEmpty():
            return None
        if i >= self.size():
            return None
        if (i + self.length) < 0:
            return None
        if i < 0:
            ind = i + self.length
        else:
            ind = i
        curr = self.head
        prev = None
        count = 0
        found = False
        while curr is not None:
            if count == ind:
                found = True
                break
            prev = curr
            curr = curr.next
            count += 1
        if found:
            node = curr.data
            if prev is None:
                self.head = self.head.next
            else:
                prev.next = curr.next
                curr.next = None
            self.length -= 1
            return node
        return None

    def insert(self, data, index):
        """ Insert data at given index in the linked list"""
        if not isinstance(index, int):
            print("Index should be of type Integer, str() passed")
            return False
        if index < 0 or index > self.size():
            print("Bad Index Range!")
            return False
        curr = self.head
        prev = None
        count = 0
        node = Node(data)

        if index == self.size():
            print("Inserting at tail")
            self.tail.next = node
            self.tail = self.tail.next
            self.length += 1
            return True

        while curr is not None:
            if count == index:
                break
            prev = curr
            curr = curr.next
            count += 1
        if prev is None:
            print("Inserting at head")
            node.next = self.head
            self.head = node
        else:
            print("Inserting in between: ", count)
            node.next = curr
            prev.next = node
        self.length += 1
        return True

    def index(self, x):
        """ return the index in the linked list of the first item
        whose value is x.
        Returns "None" if no such item in linked list """
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == x:
                return index
            curr = curr.next
            index += 1
        return None

    def append(self, data):
        """ add the data at the end of the linked list """
        node = Node(data)
        # If first node in the list then both head n tail should point to it
        if self.isEmpty():
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1

    def search(self, key):
        """Search for key and if found return the index. return -1 otherwise"""
        current = self.head
        index = 0
        found = False
        while current is not None:
            if key == current.data:
                found = True
                return index
            current = current.next
            index += 1
        if found:
            return index
        return -1

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        sll = []
        curr = self.head
        while curr is not None:
            sll.append(curr.data)
            curr = curr.next
        #print (sll)
        return sll

if __name__ == '__main__':
    mylist = LinkedList()

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
    print(mylist.slice(0, 4))
    print(mylist.index(31))
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.__str__())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
