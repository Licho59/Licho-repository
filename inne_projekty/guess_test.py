# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:16:40 2017

@author: Leszek
"""

# Gra z komputerem w zgadywanie liczb.

import random

guess_num = 0

print('What is your name?')
my_name = input()

number = random.randint(1, 20)  
print('Guess ' + my_name.title() + ', a number between 1 and 20')

while guess_num < 6:
    print('Take a guess.')
    guess = int(input())
    guess_num += 1
    
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    guess_num = str(guess_num)
    print('Gratulations ' + my_name.title() + ', you guessed the number in ' +
    guess_num + ' guesses')
if guess != number:
    print('I am sorry ' + my_name + ', the number I was thinking was ' + number)
    


    