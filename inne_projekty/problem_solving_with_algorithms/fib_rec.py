from functools import lru_cache


@lru_cache(maxsize=1000) # cache keeps the earlier computed fibonacci numbers
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 500):
    print(n, ':', fibonacci(n))
