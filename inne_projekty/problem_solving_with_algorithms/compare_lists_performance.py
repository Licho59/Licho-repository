# Design and implement an experiment that will compare the performance of a Python list with a list implemented as a linked list.
import timeit
import random

from unordered_complete_linkedList import LinkedList

def test1():
    '''Creating linkedList'''
    L = LinkedList()
    for i in range(10000):
        L.add(i)
    return L
        
def test2():
    '''Creating Python list'''
    L = []
    for i in range(10000):
        L.append(i)
    return L
        
def test3():
    '''Removing random item from linkedList'''
    L = test1()
    elm = random.choice(range(10000))
    L.remove(elm)
    
def test4():
    '''Removing random item from Python list'''
    L = test2()
    elm = random.choice(range(10000))
    L.remove(elm)
        
t1 = timeit.Timer("test1()", "from __main__ import test1")
#print("LinkedList creation ", t1.timeit(number=1000), " milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
#print("Python list creation ", t2.timeit(number=1000), " milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
#print("LinkedList removing ", t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4", "from __main__ import test4")
#print("Python removing time: ", t4.timeit(number=1000), "milliseconds")

print("\t\t\t\t\tLinkedList\t\t\tPython list")
print("List creation: ", t1.timeit(number=1000)/1000,"\t", t2.timeit(number=1000)/10000)
print("Removing func: ", t3.timeit(number=1000)/1000, "\t", t4.timeit(number=1000)/10000)
