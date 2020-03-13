int_number = int(input())
list_divisors = [1]
sum_of_divisisors = 0

for i in range(2, int_number//2):
    if int_number % 2 == 0:
        list_divisors.append(int_number)

def main():
    sum_of_divisisors = sum(list_divisors)

print('Sum of divisors of number', str(int_number), 'is ', sum_of_divisiors))
