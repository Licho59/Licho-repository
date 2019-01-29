def queensAttack(n, k, r_q, c_q, obstacles):
    result = 0
    double = [r_q, c_q]
    count = 0

    for i in range(1, c_q):
        double = [r_q, c_q - i]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, n - c_q + 1):
        double = [r_q, c_q + i]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, r_q):
        double = [r_q - i, c_q]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, n - r_q + 1):
        double = [r_q + i, c_q]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, min(r_q - 1, c_q - 1) + 1):
        double = [r_q - i, c_q - i]
        if double in obstacles:
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, min((n - r_q), (n - c_q)) + 1):
        double = [r_q + i, c_q + i]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, min(r_q - 1, n - c_q) + 1):
        double = [r_q - i, c_q + i]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    for i in range(1, min(n - r_q, c_q - 1) + 1):
        double = [r_q + i, c_q - i]
        if double in obstacles:
            count += 1
            break
        else:
            result += 1
        if count > k:
            return result
    return result


if __name__ == "__main__":
    n, k = 4, 0
    r_q, c_q = 4, 4
    obstacles = []

    '''n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)'''
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
