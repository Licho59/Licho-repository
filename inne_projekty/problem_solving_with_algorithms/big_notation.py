import time
from random import randrange


def testminList_1(L): # function name changed deliberately to check py.test command
    minimum = L[0]
    for i in range(len(L)):
        if L[i] < minimum:
            minimum = L[i]
    return minimum


def minList_2(L):
    for i in L:
        issmallest = True
        for j in L:
            if i > j:
                issmallest = False
        if issmallest:
            break
    return i


for listSize in range(1000, 10001, 1000):
    L = [randrange(100000) for x in range(listSize)]
    start = time.time()
    minList_1(L)
    print(minList_1(L))
    end = time.time()
    print("size_of_list: {:d}, time_spent_for_counting: {:.7f}".format(listSize, end - start))
