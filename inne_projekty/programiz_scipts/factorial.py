#! python3.6
# factorial.py - multiplies all integers from 1 to given number


def factorial(number):
    result = 1
    for n in range(1, number+1):
        result *= n
    return str(result)
while True:
    number = int(input('Enter the integer number to get its factorial: \n'))
    if number < 0:
        print('Wrong number - factorial for negative numbers does not exist!')
    else:
        print('Factorial value of', number, '=', factorial(number))
    cont = input('Do you want to continue?(y/n)')
    if cont == 'y':
        continue
    else:
        break
    

