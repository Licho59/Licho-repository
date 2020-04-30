# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:47:57 2017

@author: Leszek
"""
from time import time
start = time()

def primesFn():
    lista = []
    prim = 1
    while len(lista) < 10000:
        prim += 1
        for p in lista:
            if prim % p == 0:
                break
        else:
            lista.append(prim)
    return lista

primes = primesFn()
print(primes)
print()
print(time() - start)