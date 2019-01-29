import timeit
#from timeit import *
import random

from sorting_bubble_sort import bubbleSort
from sorting_insertion_sort import insertionSort
from sorting_selection_sort import selectionSort
from sorting_shell_sort import shellSort
from sorting_merge_sort import mergeSort
from sorting_quick_sort import quickSort


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def costly_func(lst):
    return map(lambda x: x ^ 2, lst)


if __name__ == '__main__':
    rand_num = []
    for i in range(1000):
        rand_num.append(random.randrange(0,100))
    #print(rand_num)
    short_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*100
    rev_short = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]*100
    for func in [bubbleSort, insertionSort, selectionSort, quickSort, shellSort, mergeSort]:
        print(func.__name__,)
        for elm in [short_list, rev_short]:
            wrapped = wrapper(func, elm)
            print(timeit.timeit(wrapped, number=1000), end =' ')
        print()
    
    
    
    
    
    
    '''t1 = Timer("bubbleSort(rand_num)", "from __main__ import bubbleSort")
    t2 = Timer("mergeSort([3,4,6,8,2])", "from __main__ import mergeSort")
    t3 = Timer("quickSort([3,4,6,8,2])", "from __main__ import quickSort")
    print("bubbleSort:", t1.timeit(10**3),"\n", "mergeSort:", t2.timeit(10**3), "\n", "quickSort:", t3.timeit(10**3))'''
