def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x/y
    else:
        print('No zero dividing')

print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

while True:
    operation = int(input('Write the number of operation (1/2/3/4)\n'))
    num1 = int(input('Enter the first number\n'))
    num2 = int(input('Enter the second number\n'))


    if operation == 1:
        print(num1, '+', num2, '=', add(num1,num2))
    elif operation == 2:
        print(num1, '-', num2, '=', subtract(num1,num2))
    elif operation == 3:
        print(num1, '*', num2, '=', multiply(num1,num2))
    elif operation == 4:
        print(num1, '/', num2, '=', divide(num1,num2))
    else:
        print('Invalid input')

    ask = input('Do you want to continue?(y/n)')
    if ask == 'y':
        continue
    else:
        break



