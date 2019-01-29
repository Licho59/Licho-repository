from timeit import Timer


def fib(n):
    '''Recursive fibonacci function.'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibi(n):
    '''Iterative fibonacci function.'''
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n - 1):
        old, new = new, old + new
    return new
    
# using the dictionary improves fib() efficiency amazingly!
memo = {0: 0, 1: 1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n - 1) + fibm(n - 2)
    return memo[n]
    
# using the class makes algorithm more compact - with dictionary inside
class Fibonacci():
    
    def __init__(self, i1=0, i2=1):
        self.memo = {0: i1, 1: i2}
        
    def __call__(self, n):
        if not n in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memo[n]

fib = Fibonacci()
for i in range(11):
    print(i, fib(i))    

if __name__ == '__main__':
    for i in range(1, 21):
        s = "fibm(" + str(i) + ")"
        t1 = Timer(s, "from __main__ import fibm")
        time1 = t1.timeit(3)
        s = "fibi(" + str(i) + ")"
        t2 = Timer(s, "from __main__ import fibi")
        time2 = t2.timeit(3)
        print("n={:2d}, fibm:{:8.6f}, fibi:   {:7.6f}, percent: {:10.2f}".format(i, time1, time2, time1 / time2))
