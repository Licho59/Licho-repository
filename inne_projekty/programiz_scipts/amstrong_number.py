#! python3.6

# amstrong_number.py - checking if given number is an amstrong number

def amstrong_number(number):

    ciphers = list(map(int, str(number)))
    k = len(ciphers)

    result = sum([num ** k for num in ciphers])

    if result == int(number):
        print('Hurra! The number', number, 'is an Amstrong number\n')
    else:
        print('Sorry,', number, 'is not an Amstrong number.\n')

if __name__ == '__main__':
    while True:
        number = int(input('\nEnter the arbitrary number: '))
        amstrong_number(number)
        stop = input('\nDo you want to continue?(y/n)')
        if stop == 'y':
            continue
        else:
            break
    
    

