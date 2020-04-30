# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:58:00 2017

@author: Leszek
"""
# Comparison of two methods for counting Fibbonachi numbers.
def fib(n):
    '''Uses recursive method.'''
    global numFibCalls
    numFibCalls = 0
    numFibCalls += 1  
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_efficient(n, d):
    '''Uses dictionary to remember earlier counted fib_numbers.'''
    global numFibCalls
    numFibCalls += 1    
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
    return ans

numFibCalls = 0
argToUse = 36

d = {1: 1, 2: 2}
print('fib(' + str(argToUse) + ') = ' + str(fib_efficient(argToUse, d)))
print('Function calls: ', numFibCalls)
print('')

numFibCalls = 0

print('fib(' + str(argToUse) + ') = ' + str(fib(argToUse)))
print('Function calls: ', numFibCalls)