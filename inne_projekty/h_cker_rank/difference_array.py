
def arrayManipulation(n,queries):
    A = [0] * n
    D = [(0 if i==0 else 0) for i in range(n+1)]
    
    for i in range(len(queries)):
        l, r, k = queries[i]
        D[l-1] += k
        D[r] -= k
        
    print(D)
    
    max = x = 0
    for i in D:
        x = x + i
        if max<x: max=x
        
    return max      

n = 10
queries = [[2,4,10],[1,5,20],[3,6,30]]
A = arrayManipulation(n, queries)
print(A)
