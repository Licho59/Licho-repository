# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:21:50 2017

@author: Leszek
"""
from time import time
start = time()
lp = 0
prim = 2
while lp < 1000:
    print(prim, end=' ')
    prim += 1
    d = 2
    while d < prim:
        if prim % d != 0:
            d += 1
        else:
            prim += 1
            d = 2
    lp += 1

print()
print(time() - start)