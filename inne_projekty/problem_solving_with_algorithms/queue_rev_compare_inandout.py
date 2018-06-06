from queue_class_rev import QueueADT
from queue_class import Queue
import datetime as dt
import time


def testQueueADT():
    """Comparing average times for enqueue and dequeue methods for Queue class with reversed way(rear of the queue is at the end of the list)"""
    Q = QueueADT()
    times = []
    NUMS = [1000, 10000, 100000, 1000000]
    for N in NUMS:
        Q = Queue()
        start = dt.datetime.now()
        for i in range(N):
            Q.enqueue(i)
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds * 1000) / N
        print("Enqueue for %d items: %d" % (1000, elapsed))

    print("==================================================")
    times = []
    for N in NUMS:
        Q = Queue()
        for i in range(N):
            Q.enqueue(i)
        start = dt.datetime.now()
        for i in range(N):
            Q.dequeue()
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds * 1000) / N
        print("Dequeue for %d items: %d" % (1000, elapsed))
        

def testQueue():
    """Comparing average times for enqueue and dequeue methods for Queue class (end of the queue is at the beginning of the list)"""
    Q = Queue()
    times = []
    NUMS = [1000, 10000, 100000, 1000000]
    for N in NUMS:
        Q = Queue()
        start = dt.datetime.now()
        for i in range(N):
            Q.enqueue(i)
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds * 1000) / N
        print("Enqueue for %d items: %d" % (1000, elapsed))

    print("==================================================")
    times = []
    for N in NUMS:
        Q = Queue()
        for i in range(N):
            Q.enqueue(i)
        start = dt.datetime.now()
        for i in range(N):
            Q.dequeue()
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds * 1000) / N
        print("Dequeue for %d items: %d" % (1000, elapsed))


def main():
    print('First test - classical implementation of queue')
    testQueueADT()
    print('-'*30)
    print('Second test - queue with list implementation')
    testQueue()

if __name__ == '__main__':
    main()
