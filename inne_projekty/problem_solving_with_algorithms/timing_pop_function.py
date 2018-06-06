import timeit

'''The measure firstly involves initiating Timer object with parameters in strings: measured operation 'pop' for concrete instance of list and importing instance of list. Secondly calling Timer object with measurement method ie. 'timeit'.'''

popzero = timeit.Timer('x.pop(0)', 'from __main__ import x') # O(n) efficiency
popend = timeit.Timer('x.pop()', 'from __main__ import x') # O(1) efficiency

'''x = list(range(2000000))

print("Time taken for popping first element of 2 mln length's list: ", popzero.timeit(number=1000))
print("\nTime taken for popping last element of 2 mln length's list: ", popend.timeit(number=1000))'''

print("pop(0)   pop()")
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz, pt))
