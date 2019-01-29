def pascalTriangle(n):
    if n == 1:
        return [1]
    else:
        last_line = pascalTriangle(n - 1)
        new_line = [1]
        for i in range(1, n - 1):
            new_line.append(last_line[i - 1] + last_line[i])
        new_line += [1]
        return new_line
        
def drawPascalTriangle(n):
    ps = []
    for i in range(1, n + 1):
        ps.append(pascalTriangle(i))
    max = len(' '.join(map(str, ps[-1])))
    for p in ps:
        print(' '.join(map(str, p)).center(max))
    return ps
        

def fibonacciCalculator(n):
    '''Fibonacci number counted by summing numbers from Pascal triangle in diagonal direction, starting from the last row corner'''
    f_n = 0
    row, col = n, 0
    triangle = drawPascalTriangle(n)
    while col < row:
        #f_n += pascalTriangle(row)[col] 
        f_n += triangle[row-1][col]
        row -= 1
        col += 1
    return f_n
    

from math import factorial
def pascal_coef(n):
    lines = []
    for i in range(n):
        line = []
        for k in range(i + 1):
            line.append(int(factorial(i) / (factorial(k) * factorial(i - k))))
        #line = ' '.join([str(i) for i in line])
        lines.append(line)

    max = len(' '.join(map(str, lines[-1])))
    for line in lines:
        print(' '.join(map(str, line)).center(max))


pascal_coef(5)

n = 10
print()
print("Fibonacci number of ", n, "counted from Pascal Triangle:",fibonacciCalculator(n))
