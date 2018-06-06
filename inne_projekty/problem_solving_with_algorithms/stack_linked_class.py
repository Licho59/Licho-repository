class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.head = None
        self.length = 0
        
    def __str__(self):
        stack_list = []
        current = self.head
        while current != None:
            stack_list.append(current.data)
            current = current.next
        return stack_list
    
    def size(self):
        return self.length
        
    def isEmpty(self):
        return self.length == 0
        
    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length += 1
    
    def pop(self):
        if self.head != None:
            node = self.head
            self.head = self.head.next
            self.length -= 1
        return node.data
        
if __name__== '__main__':        
    mylist = Stack()

    mylist.push(10)
    mylist.push(20)
    mylist.push(30)
    print(mylist.size())
    print(mylist.__str__())
    print(mylist.pop())
    print(mylist.size())
    print(mylist.__str__())

        
