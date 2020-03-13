for m in range(10):

    int_number = int(input())
    list_divisors = [1]
    sum_of_divisors = 0

    for i in range(2, (int_number//2)+1):
        if int_number % i == 0:
            list_divisors.append(i)


    list_divisors.append(int_number)

    sum_of_divisors = sum(list_divisors)


    print(list_divisors)
    print('Sum of divisors of number', str(int_number), 'is ', sum_of_divisors)


