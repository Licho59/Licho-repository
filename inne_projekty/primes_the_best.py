from time import time
start = time()

from math import sqrt

def prime_num(n):
    '''Implemented a function for the sieve of Eratosthenes. Comparable algorithm with 'sieve' function'''
    
    #all_num = [i for i in range(2, n+1)]
    all_num = list(range(2, n+1))
        
    for k in all_num:
        i = 2
       # while k*i < max:
        while k * i <= all_num[-1]:
            if k * i in all_num:
                all_num.remove(k * i)
                i += 1
            else:
                i += 1
    return all_num
    

def sieve(n):
	'''Returns all primes between 2 and n'''
	
    primes = list(range(2, n + 1))
	max = sqrt(n)
	num = 2
	while num < max:
		i = num
		while i <= n:
			i += num
			if i in primes:
				primes.remove(i)
		for j in primes:
			if j > num:
				num = j
				break
	return primes


def primes(n):
    '''With recurrency algorithm a little slower for numbers lower than sth like 40000. Efficiency is sth like O(nlogn)'''
    
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i * 2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(40000))


#print(sieve(40000))

'''n = 40000
primes = prime_num(n)
print(primes)
print()
print(time() - start)'''
