"""
Taken from https://www.python-course.eu/python3_recursive_functions.php
- very fast algorithm using  resursive way of building Pascal Triangle and at the same time counting Fibonacci number, starting from upper-right part of triangle down to bottom left corner of n level.
"""

def fib_pascal(n, fib_pos):
    if n == 1:
        line = [1]
        print(*line)
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n - 1, fib_pos + 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
        print(*line)
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)


def fib(n):
    return fib_pascal(n, 0)[1]


# and now printing out the first ten Fibonacci numbers:
#for i in range(1, 200):
 #   print(fib(i))
n = 20
print()
print("Fibonacci number of n =", n, ":", fib(n))
