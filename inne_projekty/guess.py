# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 13:34:33 2017

@author: Leszek
"""
# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName.title() + ' I am thinking about a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess is too low.')
        
    if guess > number:
        print('Your guess i too high.')
        
    if guess == number:
        break

if guess == number:
    print('Good job, ' + myName.title() + '! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
        
