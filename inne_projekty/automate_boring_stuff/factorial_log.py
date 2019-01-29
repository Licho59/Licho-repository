#! python3
# 'factorial_log.py' - program to count factorials but also showing logs of messages

import logging
# easy to stop working logging by using logging.disable() function
#logging.disable(logging.CRITICAL)

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# using filename argument to keep screen clear by writing logging messages to a file 
#logging.basicConfig(filename='factorial_log.txt', level=logging.DEBUG, format=' {asctime} - {levelname} - {message}', style='{')

# string formating in {}.format style
logging.basicConfig(level=logging.DEBUG, format=' {asctime} - {levelname} - {message}', style='{')
logging.debug('Start of the program')

def factorial(n):
    logging.debug('Start of factorial({})'.format(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')


                    
