def knapsack(wt, val, W, n):
    """Returns the max value of items (of individual weights and values according to wt and val lists) which can be put to knapsack of W amount"""
    
    T = [[0 for i in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            elif wt[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                m = j - wt[i - 1] #unnecessary
                k = T[i - 1][m] #unnecessary
                T[i][j] = max(T[i - 1][j], T[i - 1]
                              [j - wt[i - 1]] + val[i - 1])
    return T[n][W]


val = [3, 4, 8, 8, 10]
wt = [2, 3, 4, 5, 9]
W = 20
n = len(val)
print(knapsack(wt, val, W, n))
