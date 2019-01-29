"""
Write a recursive function find_index(), which returns the index of a number in the Fibonacci sequence, if the number is an element of this sequence and returns -1 if the number is not contained in it, i.e.
"""
from timeit import Timer
#import timeit

memo = {0:0, 1:1}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

def find_index_iter(n): # it is iterative function
    for i in range(2, n+1):
        if fib(i) < n:
            continue
        elif fib(i) == n:
            return i
        else:
            return -1
            
            
def find_index(*x): # it is recursive function
	""" finds the natural number i with fib(i) = n """
	if len(x) == 1:
		# started by user
		# find index starting from 0
		return find_index(x[0], 0)
	else:
		k = fib(x[1])
		m = x[0]
		if k > m:
			return -1
		elif k == m:
			return x[1]
		else:
			return find_index(m, x[1] + 1)
			
# Instructions for checking the position of fibonacci number being the result of squares two consecutive fibbonacci numbers
print(" index of a |    a |     b | sum of squares | index ")
print("=====================================================")
for i in range(15):
	square = fib(i)**2 + fib(i + 1)**2
	print(" %10d |  %3d |   %3d | %14d | %5d " %
	      (i, fib(i), fib(i + 1), square, find_index(square)))
			
# Functions for testing the quickness of earlier algorithms
n = fib(500)
def f_test1():
	find_index_iter(n)
	
def f_test2():
	find_index(n)
	

if __name__ == '__main__':
	n = 500
	k = 3            
	print("fibonacci of ", n, "\n", fib(n))
	print()
	print("Finding fibonacci index functions:")
	t1 = Timer("find_index_iter", "from __main__ import find_index_iter")
	t2 = Timer("find_index", "from __main__ import find_index")
	print("Iterative: ", t1.timeit(10**k),"\nRecursive: ", t2.timeit(10**k))
	
	#print(timeit.timeit("f_test1", "from __main__ import f_test1"))
	#print(timeit.timeit("f_test2", "from __main__ import f_test2"))
	
	#print(find_index_iter(n))
	#print(find_index(n))


