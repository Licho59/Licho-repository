def flatlandSpaceStations(n, c):
    c = sorted(c)
    last = 0
    res = c[0]
    for x in c:
        res = max(res, (x - last) / 2)
        last = x
    res = max(res, (n - 1 - last))
    return res


if __name__ == "__main__":
    n, m = 95, 19
    c = [68, 81, 46, 54, 30, 11, 19, 23, 22,
         12, 38, 91, 48, 75, 26, 86, 29, 83, 62]
    '''n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))'''
    result = flatlandSpaceStations(n, c)
    print(result)
