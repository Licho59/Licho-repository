# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:24:12 2017

@author: Leszek
"""
# This program says hello and asks for my name

import fire

print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)

fire.Fire()
