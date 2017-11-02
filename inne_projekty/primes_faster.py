# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:21:48 2017

@author: Leszek
"""
from time import time
start = time()

prim = 2
list = []
while len(list) < 1000:
    print(prim, end=' ')
    prim += 1
    p = 2
    i = 0
    while i < len(list):
        if prim % list[i] != 0:
            i = i+1
            continue
        else:
            prim += 1
            i = 0
    list.append(prim)

print()    
print(time() - start)