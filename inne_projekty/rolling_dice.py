"""Guess the number"""

import random

def check_input(value):
    if value is int:
        return int(value)
    else:
        return 'You have given wrong value'
    

def make_random():
    return random.randint(1, 100)
    
def give_number():
    number = input("Give the number between 1 and 100 included: ")
    check_input(number)
    isgood((int(number)))

def isgood(value):
    to_guess = make_random()
    if value == to_guess:
        print('Gratulations - you guessed the number')
        while True:
            ask = input('Do you want to play again? (y/n)')
            if ask == 'y':
                give_number()
            else:
                break
    else:
        if value < to_guess:
            print('Too low')
            give_number()
        else:
            print('Too high')
            give_number()


give_number()
    



