"""An algorithm for finding both the minimum and maximum of n
numbers using fewer than 3n/2 comparisons."""

import random

N = 20
numbers = []
for i in range(10):
    m = random.randint(1, N)
    numbers.append(m)

maximum = 0
minimum = N
result = [minimum, maximum]

for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
    else:
        if numbers[i] < minimum:
            minimum = numbers[i]
result = [minimum, maximum]

print(result)
