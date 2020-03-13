def factors_set():
    factors_set = ( (i, j, k, l) for i in [-1, 0, 1] 
                          for j in [-1, 0, 1]
                          for k in [-1, 0, 1]
                          for l in [-1, 0, 1])
    for factor in factors_set:
        yield factor

def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

@memoize
def linear_combination(n):
    """ returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27      """
    weighs = (1,3,9,27)
    
    if n > 40:
        return f'Not enough weights to weigh {n} kg thing!'
    for factors in factors_set():
       sum = 0
       for i in range(len(factors)):
          sum += factors[i] * weighs[i]
       if sum == n:
          weight_factors = factors
          return [weighs[i]* weight_factors[i]
                  for i in range(len(weighs)) if weight_factors[i] != 0]

for n in range(20, 44):
    factors = linear_combination(n)
    print(factors)
    
    
    
