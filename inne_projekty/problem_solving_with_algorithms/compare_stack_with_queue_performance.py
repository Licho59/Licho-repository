#Design and implement an experiment that will compare the performance of the Python list based stack and queue with the linked list implementation.
from timeit import Timer

from stack_linked_class import Stack
from queue_linked_class import Queue

def test1():
    '''Adding element to the stack'''
    tested_stack = Stack()
    elm = random.choice(range(1000))
    tested_stack.push(elm)
    return tested_stack
    
def test2():
    '''Adding element to the queue'''
    tested_queue = Queue()
    elm = random.choice(range(1000))
    tested_queue.enqueue(elm)
    return tested_queue
    
def test3():
    '''Removing element from the stack'''
    L = test1()
    L.pop()
    
def test4():
    '''Removing element from the queue'''
    L = test2()
    L.dequeue()
    
    
if __name__ == '__main__':
    print("Type of structure\t\t\tStack\t\t\t\tQueue")    
    t1 = Timer("test1", "from __main__ import test1")
    t2 = Timer("test2", "from __main__ import test2")
    t3= Timer("test3", "from __main__ import test3")
    t4 = Timer("test4", "from __main__ import test4")
    
    print("Adding element: ", "\t\t", "%.7f" % round(t1.timeit(), 7), "\t\t\t", "{0:.7f}".format(t2.timeit(number=1000000)))
    print("Removing element: ", "\t\t", "{0:7f}".format(t3.timeit()), "\t\t\t", "{0:7f}".format(t4.timeit()))

