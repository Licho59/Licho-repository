def flatlandSpaceStations(n, c):
    all_cities = list(range(n))
    for elm in c:
        all_cities[elm] = 's'
    first_max, k_max, last_max = 0, 0, 0
    k = 0
    if all_cities[0] != 's':
        for elm in all_cities:
            if elm == 's':
                if k > first_max:
                    first_max = k
                    break
            else:
                k += 1
                continue
    k = 0
    for elm in all_cities:
        if elm == 's':
            if k > k_max:
                k_max = k
            k = 0
            continue
        else:
            k += 1
            continue
    if k > k_max:
        last_max = k
    if k_max % 2 == 0:
        k_max = k_max // 2
    else:
        k_max = k_max // 2 + 1

    return max(first_max, k_max, last_max)


if __name__ == "__main__":
    n, m = 99998, 5
    c = [28000, 58701, 43043, 24909, 28572]
    '''n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))'''
    result = flatlandSpaceStations(n, c)
    print(result)
