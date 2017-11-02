# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:44:16 2017

@author: Leszek
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    while L1 == [] and L2 == []:
        return (None, None, None)
    else:
        if len(L1) != len(L2):
            return False
    C = L2[:]
    for elm in L1:        
        if elm in C:
            C.remove(elm)
        else:
            return False
            
    temp = {}
    for elm in L1:
        while elm in L2:
            if elm in temp:        
                temp[elm] += 1
            else:
                temp[elm] = 1
            break
        else:
            return False
    maksimum = 0
    for k in temp.keys():
        if temp[k] >= maksimum:
            maksimum = temp[k]
    for k in temp:
        if temp[k] == maksimum:
            return (k, maksimum, type(k)) 
    
L1 = [0, 4, 8, 3, 0, 2, 2, 1, 4, 7, 8, 3, 7, 0, 0]
L2 = [3, 4, 0, 3, 8, 0, 2, 0, 7, 2, 0, 3, 7, 2, 1]
print(is_list_permutation(L1, L2))