# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:42:37 2017

@author: Leszek
"""
# debugowanie pliku - nauka
import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
    print('Correct!')
else:
    print('Noup! The answer is ' + str(number1 + number2))