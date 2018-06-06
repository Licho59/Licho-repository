import timeit
import random
'''For comparing how long it takes for 'contains' operation both list and dictionary.'''
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000) # for list O(n) efficiency
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)  # for dictionary O(1) efficiency
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time)) # can be shown with matplotlib plot
