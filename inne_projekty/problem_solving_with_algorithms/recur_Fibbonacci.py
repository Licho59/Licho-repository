"""Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?"""
def recFib(N):
    global count_rec
    count_rec += 1
    
    if N == 1 or N == 2:
        return 1
    else:
        return recFib(N-1) + recFib(N-2)

count_rec = 0
print(recFib(26))
print("Number of recursive calls: ", count_rec)
                    