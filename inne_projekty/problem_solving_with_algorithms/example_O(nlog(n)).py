#Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
import timeit
import random
import matplotlib.pyplot as plt

smallest = timeit.Timer("sorted(unord_list)[k]", "from __main__ import unord_list, k") # two operations: sorting(O(nlog(n)) and finding index(O(1))
all = []
for i in range(100, 15000, 100):
    k = random.randrange(99)
    unord_list = [random.randrange(i) for j in range(i)]
    time_smallest = smallest.timeit(number=1000)
    all.append(time_smallest)
    print("{0} {1:10.6f}".format(i, time_smallest)) # algorithm is O(nlog(n))

plt.plot([i for i in range(100, 15000, 100)], all, 'ro')
plt.axis([0, 15000, 0, 10])
plt.show()
    
