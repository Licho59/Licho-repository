"""Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?"""

counter = 0
def recFib(N):    
    global counter
    if N == 1 or N == 2:
        return 1
    else:
        counter += 2
        return recFib(N-1) + recFib(N-2)


def iterFib(N):
    fibs = [0, 1]
    for j in range(2, N + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def countDigits(k):
    length = 0
    N = 1
    while length < k:
        N += 1
        fibs = iterFib(N)
        length = len(str(fibs[-1]))
    print(N, fibs[-1], length)


fib_lev = 26
print("For recurency level " + str(fib_lev) + " Fibbonaci number = " + str(recFib(26)))
print("Number of recursive calls: ", counter)
print()

print("For iteration level " + str(fib_lev) + " Fibbonaci number = " + str(iterFib(fib_lev)[-1]))
print()

print("Fibbonaci level and number with respective amount of digits:")         

countDigits(500)           
