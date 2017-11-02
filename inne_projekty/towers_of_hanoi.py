# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:12:29 2017

@author: Leszek
"""

def printMove(fr, to):
    print('Move from ' + str(fr) + 'to ' + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(4, 'P1', 'P2', 'P3'))