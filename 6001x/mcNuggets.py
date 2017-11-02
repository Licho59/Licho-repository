# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:52:33 2017

@author: Leszek
"""

def McNuggets(n):
    """
    n is an int
                    6a + 9b + 20c = n
    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a, b, c = 0, 0, 0
    suma = 0
    while suma < n:
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    suma = 6*a + 9*b + 20*c
                    if suma == n:
                        return True
                    elif suma < n:
                        continue
                    else:
                        break
        else:
            return False
            
print(McNuggets(133))